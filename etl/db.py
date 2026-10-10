from sqlmodel import SQLModel, Field, Session, create_engine
from datetime import datetime
from functools import cache

class DBSource(SQLModel, table=True):
    __tablename__ = "sources"

    id: int | None = Field(default=None, primary_key=True)
    distro: str
    version: str | None
    bundle: str | None
    last_checked: datetime | None
    last_processed: datetime | None
    last_ref: str | None
    config: str

class DBPackage(SQLModel, table=True):
    __tablename__ = "packages"
    
    id: int | None = Field(default=None, primary_key=True)
    source: int  #TODO: Foreign Key
    name: str

class DBPackageVersion(SQLModel, table=True):
    __tablename__ = 'packageVersions'
    
    id: int | None = Field(default=None, primary_key=True)
    package: int   #TODO: Foreign Key
    version: str
    first_seen: datetime

@cache
def get_db(url):
    return create_engine(url)

def get_session(url):
    return Session(get_db(url))
