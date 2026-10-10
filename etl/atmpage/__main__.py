from . import get_repo

import logging
logging.basicConfig(level=logging.DEBUG)

repo = get_repo("type=apkv3;url=https://repo.chimera-linux.org/current/main;trust_time=True;allow_untrusted=True")
    
print(repo._apk(('update',)))
listing = (repo.apk_list('*-man'))
print(list(listing))
