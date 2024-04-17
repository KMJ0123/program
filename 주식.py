#20244043 김민주
print('20244043 김민주')

import requests
from bs4 import BeautifulSoup
from urllib import request, parse

token = 'ZQAAAYEDIPngExdltTFMb-dmKO5rfejy7M3oHAvmKlpTY8pYinUnQ0C2cGVNjFG0k9yLSjHjC4uOony32LbEkWTGST9fPprrY3Sn6oT8beOaRaQf'
band_key = 'AAAya6jGF4MUx5TXLm7eSun8'

def send_to_Band(bk, content, do_push=True):
    url = 'https://openapi.band.us/v2.2/band/post/create'
    data = {'access_token': token, 'band_key': bk, 'content': content, 'do_push': do_push}
    response = requests.post(url, data=data)
    if response.status_code == 200:
        print(f'전송완료: {content}')
    else:
        print(f'전송 실패: {response.status_code}')

def get_stock_price(stock_code):
    url = f"https://finance.naver.com/item/main.nhn?code={stock_code}"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        price_element = soup.select_one('#chart_area > div.rate_info > div > p.no_today > em')
        if price_element:
            return price_element.text.strip()
        else:
            return "주식 가격을 찾을 수 없습니다."
    else:
        return f"오류 발생: {response.status_code}"

stock_check = int(input("""What stock would you like to check?
                    1. Samsung 2. LG 3. SK
                    Please enter the number: """))

stock_codes = ['005930', '003550', '017670']
stock_names = ['삼성전자', 'LG', 'SK']

if 1 <= stock_check <= len(stock_codes):
    stock_code = stock_codes[stock_check - 1]
    stock_name = stock_names[stock_check - 1]
    price = get_stock_price(stock_code)
    
else:
    print('Please choose a number from the options provided.')

send = input("""How would you like to check stock information?
             1. Band 2. file 3. Terminal
             Please enter the number: """)

if send == str(1):
    send_to_Band(band_key, f"{stock_name} 주식 가격: {price}")

elif send == str(2):
    with open("price.txt", "w") as f:
        f.write(f"{stock_name} 주식 가격: {price}")

elif send == str(3):
    print(f"{stock_name} 주식 가격: {price}")

else:
    print('Please choose a number from the options provided.')



    #주식 코드를 택스트 파일에 저장해서 실행할때 값을 가져와서 실행 여러개의 주식 값을 확인할 수 있도록 변경 그 주식을 내림차 순으로 정렬해서 출력
