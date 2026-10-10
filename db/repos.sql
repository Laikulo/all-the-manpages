DELETE FROM sources;

INSERT INTO sources
	(distro, version, bundle, config) VALUES 
	('chimera', 'current', 'main', 'type=apkv3;url=https://repo.chimera-linux.org/current/main;trust_time=True,allow_untrusted=True'),
	('chimera', 'current', 'contrib', 'type=apkv3;url=https://repo.chimera-linux.org/current/contrib;trust_time=True,allow_untrusted=True'),
	('chimera', 'current', 'user', 'type=apkv3;url=https://repo.chimera-linux.org/current/user;trust_time=True,allow_untrusted=True')
	;
