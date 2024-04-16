import json # json 모듈
from pprint import pprint # pretty print 모듈
from urllib import request # request 모듈
# 접근 토큰
token = 'ZQAAAYEDIPngExdltTFMb-dmKO5rfejy7M3oHAvmKlpTY8pYinUnQ0C2cGVNjFG0k9yLSjHjC4uOony32LbEkWTGST9fPprrY3Sn6oT8beOaRaQf'
def get_bands():
    url = f'https://openapi.band.us/v2.1/bands?access_token={token}'
    req = request.Request(url)
    res = request.urlopen(req)
    text = res.read().decode("utf8")
    json_dict = json.loads(text) # 내가 가입한 밴드 목록 딕셔너리 리턴
    return json_dict

pprint(get_bands())


