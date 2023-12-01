import requests
import json

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

API_KEY = 'xx'
API_SECRET = 'xx'
CODE = 'xx'
REDIRECT_URI = 'https://mynamecoder.com'
access_token_url = 'https://api.weibo.com/oauth2/access_token'

params = {
    'client_id': API_KEY,
    'client_secret': API_SECRET,
    'grant_type': 'authorization_code',
    'code': CODE,
    'redirect_uri': REDIRECT_URI
}


if __name__ == '__main__':
    # 1、获取code
    # https://api.weibo.com/oauth2/authorize?client_id=526292860&response_type=code&redirect_uri=https://mynamecoder.com
    # 2、根据code获取token
    res = requests.post(access_token_url, data=params)
    token = json.loads(res.text)
    print(token)
