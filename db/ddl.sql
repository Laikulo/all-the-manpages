DROP TABLE IF EXISTS sources;
CREATE TABLE sources (
	id INTEGER PRIMARY KEY,
	distro TEXT NOT NULL,
	version TEXT,
	bundle TEXT,
	last_checked DATETIME,
	last_processed DATETIME,
	last_ref TEXT,
	config TEXT
);

DROP TABLE IF EXISTS packages;
CREATE TABLE packages (
	id INTEGER PRIMARY KEY,
	source INTEGER NOT NULL REFERENCES sources(id),
	name TEXT NOT NULL
);

DROP TABLE IF EXISTS packageVersions;
CREATE TABLE packageVersions (
	id INTEGER PRIMARY KEY,
	package INTEGER NOT NULL REFERENCES packages(id),
	version TEXT NOT NULL,
	first_seen DATETIME NOT NULL,
	processed_on DATETIME
);

DROP TABLE IF EXISTS manpages;
CREATE TABLE manpages (
	id INTEGER PRIMARY KEY,
	section TEXT NOT NULL,
	title TEXT NOT NULL
);

DROP TABLE IF EXISTS manpageVersions;
CREATE TABLE manpageVersions (
	id INTEGER PRIMARY KEY,
	manpage INTEGER NOT NULL REFERENCES manpages(id),
	hash TEXT NOT NULL
);

DROP TABLE IF EXISTS rel_pVer_mVer;
CREATE TABLE rel_pVer_mVer (
	packageVer INTEGER NOT NULL REFERENCES packageVersion(id),
	manpageVer INTEGER NOT NULL REFERENCES manpageVersion(id),
	PRIMARY KEY (packageVer,manpageVer)
);

