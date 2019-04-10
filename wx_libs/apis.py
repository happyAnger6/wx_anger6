import requests, json
from .api_endpoints import access_token_url

def access_toke(appID, appsecret):
    url = access_token_url % (appID, appsecret)
    r = requests.get(url)
    j = json.load(r.text)
    return j.get('access_token', None), j.get('expires_in', None)
