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
	package INTEGER NOT NULL REFERENCES sources(id),
	version TEXT NOT NULL,
	first_seen DATETIME NOT NULL
);
