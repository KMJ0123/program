import requests
import json

#1.
tokens = 'GqbJYSCY0neqzISHpBPdt7wKtX6RgR20vDcKPXOaAAABjsex15Zb9Pmr5eg_ZA'
	

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send 

headers={"Authorization" : "Bearer " + tokens}

data={
    "template_object": json.dumps({
        "object_type":"text",
        "text":"Hello, world!",
        "link":{
            "web_url":"www.naver.com"
        }
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code
print(response.status_code)
if response.json().get('result_code') == 0:
	print('메시지를 성공적으로 보냈습니다.')
else:
	print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
