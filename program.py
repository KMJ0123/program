#20244043 김민주
print('20244043 김민주')

import requests, json, time      #requests모듈과 beautifulsoup 모듈 time모듈 가져오기
from bs4 import BeautifulSoup

def send_to_Band(a,b,c):

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

stock_code = "005930"  # 삼성전자 주식 코드

while True: #프로그램을 종료할때까지 계속 주식 가격을 알려준ㄴ 코드
    price = get_stock_price(stock_code)
    print(f"삼성전자 주식 가격: {price}")
    time.sleep(10)  # 10초마다 주식 가격 확인