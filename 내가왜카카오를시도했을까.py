import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '8e58a9c0a3c18e504ed060195b62cc8a'
redirect_uri = 'https://example.com/oauth'
authorize_code = '9UBbTQRWbpuE2Pha7naXkamIwuIAxlzZdTJ4MHtdmGu8I53SbITxVI3XGk4KPXVaAAABjseuLrmm1x-HnlkNwQ'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json
#1.
with open(r"kakao_code.json","w") as fp:
    json.dump(tokens, fp)