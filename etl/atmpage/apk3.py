from . import BaseRepo, PackageRef
from .util import get_http_timerev
from functools import cache, cached_property
from tempfile import TemporaryDirectory
from pathlib import Path
from subprocess import run as runproc

import logging
logger = logging.getLogger(__name__)

class Apk3Repo(BaseRepo):
    def __init__(self, config:dict):
        self._trust_file_time = bool(config.get('trust_time', False))
        self._url = config['url']
        self._allow_untrusted = bool(config.get('allow_untrusted', False))
        self.__tmpdir = None

    @cached_property
    def _tmpdir(self):
        self.__tmpdir = TemporaryDirectory()
        return Path(self.__tmpdir.name)

    def __cleanup():
        if self.__tmpdir:
            self._tmpdir.cleanup()
            self._tmpdir.clear_cache()
            self.__tmpdir = None

    def has_filelists(self) -> bool:
        return None

    def clear_cache(self) -> None:
        self.ref.cache_clear()

    def _make_apk_repos(self):
        repo_file = (self._tmpdir / 'apk-repositories.conf')
        if not repo_file.exists():
            repo_file.write_text(f"v3 {self._url}")
        return repo_file

    def _make_apk_skel(self):
        apk_root = self._tmpdir / 'apkroot'
        if not apk_root.exists():
            apk_root.mkdir()
            (apk_root / 'lib' / 'apk' / 'db').mkdir(parents=True)


    def _apk(self, args, auto_init=True, no_repos=False):
        apk_root = self._tmpdir / 'apkroot'
        if not apk_root.exists():
            apk_root.mkdir()
        apk_args = [ '--root', apk_root.absolute(), '--root-tmpfs=yes' ]
        if self._allow_untrusted:
            apk_args += ['--allow-untrusted']

        if not (apk_root / 'lib' / 'apk' / 'db' / 'installed').exists() and auto_init:
            logger.debug("Initaluzing APK DB")
            self._apk(('add', '', '--initdb', '--usermode'), auto_init=False, no_repos=True)

        if no_repos:
            apk_args += ['--repositories-file', "/dev/null"]
        else:
            repo_file = self._make_apk_repos()
            apk_args += ['--repositories-file', repo_file.absolute() ]

        apk_args += args
        logging.debug(f'APK: {apk_args}')
        apk_proc = runproc(('apk', *apk_args), check=True, capture_output=True)
        for line in apk_proc.stdout.splitlines():
            logging.debug(f'APKout: {line}')
        for line in apk_proc.stderr.splitlines():
            logging.debug(f'APKerr: {line}')
        return apk_proc

    def refresh(self):
        self._apk(('update',))

    def apk_list(self, query=None):
        if query:
            qargs=(query,)
        else:
            qargs=()

        proc = self._apk(('list', '--available',  *qargs))
        return((self._list_to_ref(l) for l in proc.stdout.decode().splitlines()))

    def _list_to_ref(self, list_entry):
        # Remove non-package name
        list_entry = list_entry.split(' ',1)[0]

        toks = list_entry.rsplit('-',2)
        name = toks[0]
        ver_toks = toks[1:]
        ver = "-".join(ver_toks)

        return PackageRef(self, name, ver)
        


    @cache
    def ref(self) -> None:
        if not self._trust_file_time:
            return None
        else:
            return get_http_timerev(self._url + "/Packages.adb")
    
    
