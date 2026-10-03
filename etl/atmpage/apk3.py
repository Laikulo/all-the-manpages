from . import BaseRepo
from .util import get_http_timerev
from functools import cache

class Apk3Repo(BaseRepo):
    def __init__(self, config:dict):
        self._trust_file_time = bool(config.get('trust_time', False))
        self._url = config['url']

    def has_filelists(self) -> bool:
        return None

    def clear_cache(self) -> None:
        self.ref.cache_clear()

    @cache
    def ref(self) -> None:
        if not self._trust_file_time:
            return None
        else:
            return get_http_timerev(self._url + "/Packages.adb")
    
    
