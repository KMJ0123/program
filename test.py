# import requests

# url = 'https://kauth.kakao.com/oauth/token'
# rest_api_key = '8e58a9c0a3c18e504ed060195b62cc8a'
# redirect_uri = 'https://example.com/oauth'
# authorize_code = 'AkyU7d1bASo3CbeRu-yIuMBbOfrapXI-LpLudF7afcMBWu0-8waw0CZ-mEYKKclfAAABjryeFBTdCc_9be4aqQ'

# data = {
#     'grant_type':'authorization_code',
#     'client_id':rest_api_key,
#     'redirect_uri':redirect_uri,
#     'code': authorize_code,
#     }

# response = requests.post(url, data=data)
# tokens = response.json()
# print(tokens)

# import json

# with open("kakao_code.json","w") as fp:
#     json.dump(tokens, fp)

import json

with open("kakao_code.json","r") as fp:
    ts = json.load(fp)
print(ts)
print(ts["access_token"])