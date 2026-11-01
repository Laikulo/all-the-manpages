from . import get_repo
from .db import get_session, DBSource, DBPackage, DBPackageVersion
from sqlmodel import select
from datetime import datetime
from datetime import UTC

import logging
logging.basicConfig(level=logging.DEBUG)

run_time=datetime.now(UTC)

with get_session("sqlite:////mnt/db/test.db") as session:
    db_sources = session.exec(select(DBSource))
    for src in db_sources:
        repo = get_repo(src.config)
        src.last_ref = repo.ref()
        src.last_checked = run_time
        repo.refresh()
        # Get all package name:id pairs from the DB
        src_pkgs = session.exec(select(DBPackage).where(DBPackage.source == src.id))
        pkg_ids = { p.name: p.id for p in src_pkgs }
        for pkg in repo.pkgs_with_manpages():
            if pkg.name not in pkg_ids:
                # This is less than optimal, Would be better to do these all at once
                # (make a list of all that are missing, and bulk-create, then bulk-refresh)
                new_pkg = DBPackage(source=src.id, name=pkg.name)
                session.add(new_pkg)
                session.flush()
                session.refresh(new_pkg)
                pkg_id = new_pkg.id
            else:
                pkg_id = pkg_ids[pkg.name]
            this_vers = session.exec(select(DBPackageVersion).where(DBPackageVersion.package == pkg_id and DBPackageVersion.version == pkg.version)).one_or_none()
            if not this_vers:
                this_vers = DBPackageVersion(package=pkg_id, version=pkg.version, first_seen=run_time)
                session.add(this_vers)
        src.last_processed = run_time
        session.add(src)
    session.commit()
    # At this point, all packagevers have been populated.

