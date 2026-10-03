import requests
from dateutil.parser import parse as dateparse

def get_http_time(url):
    resp = requests.head(url)
    last_mod = resp.headers.get('Last-Modified')
    if not last_mod:
        return None
    last_mod = dateparse(last_mod)
    return(last_mod)

def get_http_epoch(url):
    return int(get_http_time(url).timestamp())

def get_http_timerev(url):
    return str(get_http_epoch(url))

