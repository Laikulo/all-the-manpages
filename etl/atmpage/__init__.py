from abc import ABC, abstractmethod
from typing import Optional
from dataclasses import dataclass

class BaseRepo(ABC):

    def __init__(self, config_data: dict):
        pass


    @abstractmethod
    def ref(self) -> Optional[str]: 
        """
            Retuns the reference of the remote repository.
            This is an opaque string, and is stored in the DB to aviod requesting a
            repository that has already been processed.
            Returns None if th remote does not have such a field that can be determined without
            fetching
        """
        ...

    @abstractmethod
    def has_filelists(self)  -> bool:
        """
            Returns true if the repo supports filelists.
            This means that file contents can be determined without downloding all packages.
        """
        ...

    @abstractmethod
    def refresh(self) -> None:
        """
            Unconditionall refresh metadata. This may result in initalizing the package manager if it was not needed earlier.
        """
        ...


@dataclass
class PackageRef:
    repo: BaseRepo
    """
    The repo object this Ref is from
    """

    name: str
    """
    The name of the targeted package
    """

    version: str
    """
    opaque version string for the package. may not be the same as what the packge ecosystem calls a version
    """


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

