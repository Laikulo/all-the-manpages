from abc import ABC, abstractmethod
from typing import Optional

class BaseRepo(ABC):

    def __init__(self, config_data: dict):
        pass


    @abstractmethod
    def ref(self) -> Optional[str]: ...
    @abstractmethod
    def has_filelists(self)  -> bool: ...

from .apk3 import Apk3Repo

_REPO_TYPES={
        'apkv3': Apk3Repo
        }

def get_repo(config: str|dict):
    if isinstance(config,str):
        config = {t[0]:t[1] for t in [opt.split("=",1) for opt in config.split(";") ]}
    if 'type' not in config:
        raise ValueError("Repo config does not specify type")
    if config['type'] not in _REPO_TYPES:
        raise ValueError(f"Unknonw repo type {config['type']}")
    return _REPO_TYPES[config['type']](config)

repo = get_repo("type=apkv3;url=https://repo.chimera-linux.org/current/main/x86_64;trust_time=True")
    
print(repo.ref())
