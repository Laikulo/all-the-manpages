DELETE FROM sources;

INSERT INTO sources
	(distro, version, bundle, config) VALUES 
	('chimera', 'current', 'main', 'type=apkv3;url=https://repo.chimera-linux.org/current/main/x86_64'),
	('chimera', 'current', 'contrib', 'type=apkv3;url=https://repo.chimera-linux.org/current/contrib/x86_64'),
	('chimera', 'current', 'user', 'type=apkv3;url=https://repo.chimera-linux.org/current/user/x86_64')
	;
