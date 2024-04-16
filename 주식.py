#20244043 김민주
print('20244043 김민주')

import requests, json     #requests모듈과 json 모듈


from bs4 import BeautifulSoup  #Beautifulsoup
from urllib import request, parse #urllid 모듈의 request와 parse

#접근 토큰
token = 'ZQAAAYEDIPngExdltTFMb-dmKO5rfejy7M3oHAvmKlpTY8pYinUnQ0C2cGVNjFG0k9yLSjHjC4uOony32LbEkWTGST9fPprrY3Sn6oT8beOaRaQf'
band_key = 'AAAya6jGF4MUx5TXLm7eSun8' #python 밴드의 밴드 키 값

def send_to_Band(bk, content, do_push=True): #send_to_Band 함수 정의 bk=band key, content=개시물의 내용,do_push=push알림여부
    url = 'https://openapi.band.us/v2.2/band/post/create' #요청을 보낼 URL
    req = request.Request(url) #URL을 사용하여 Request객체 생성
    data = {'access_token': token, 'band_key': bk, 'content': content, 'do_push': do_push} #딕셔너리 data 생성
    post_data = parse.urlencode(data).encode('utf8')
    res = request.urlopen(req, post_data)
    print(f'전송완료,{content}')


def get_stock_price(stock_code): #get_stock_price()함수 정의 실시간 가격을 가져오는 역할을 함
    url = f"https://finance.naver.com/item/main.nhn?code={stock_code}"

    response = requests.get(url) #requests.get() 함수를 이용해 url에 get 요청을 보냄

    if response.status_code == 200: #요청에 대한 응답 여부 확인 response.status_code 가 200이면 성공적으로 응답을 받은 것
        html = response.text        #html문서를 가져온다 
        soup = BeautifulSoup(html, 'html.parser')   #BeautifulSoup 객체를 생성하여 html 문서를
        price_element = soup.select_one('#chart_area > div.rate_info > div > p.no_today > em') #BeautifulSoup을 사용하여 HTML 문서에서 실시간 주식 가격을 포함한 요소를 선택
        if price_element: #요소가 존재하는지 확인, 존재한다면 텍스트를 리턴
            return price_element.text.strip()
        else: #위의 조건문이 거짓인 경우
            return "주식 가격을 찾을 수 없습니다."
    else: #응답이 성공적이지 않은 경우
        return f"오류 발생: {response.status_code}"
    

#확인하고 싶은 주식을 선택
stock_check = input("""What stock would you like to check?
                    1. Samsung 2. LG 3. sk
                    Please enter the number""")

if stock_check == str(1): #stock_check의 값이 문자열 1인 경우
    stock_code = '005930' #삼성 주식 코드 005930를 변수에 저장
    price = get_stock_price(stock_code) #get_stock_price 함수 호출
    sam = (f"삼성전자 주식 가격: {price}") #리턴 받은 삼성 주식 가격을 문자열에 포함해 변수에 저장
    send_to_Band(band_key, sam)  #send_to_Band 함수 호출

elif stock_check == str(2): #stock_check의 값이 문자열 2인 경우
    stock_code = '003550'  #LG 주식 코드 005930를 변수에 저장
    price = get_stock_price(stock_code) #get_stock_price 함수 호출
    sam = (f"LG 주식 가격: {price}")  #리턴 받은 LG 주식 가격을 문자열에 포함해 변수에 저장
    send_to_Band(band_key, sam)  #send_to_Band 함수 호출

elif stock_check == str(3): #stock_check의 값이 문자열 1인 경우
    stock_code = '017670'   #sk 주식 코드 005930를 변수에 저장
    price = get_stock_price(stock_code)#get_stock_price 함수 호출
    sam = (f"sk 주식 가격: {price}")#리턴 받은 sk 주식 가격을 문자열에 포함해 변수에 저장
    send_to_Band(band_key, sam) #send_to_Band 함수 호출

else:
    print('제공하지않는 주식 정보 입니다.')

