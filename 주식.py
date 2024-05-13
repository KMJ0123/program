#20244043 김민주
print('20244043 김민주')

import requests, os
from bs4 import BeautifulSoup
from urllib import request, parse

token = 'ZQAAAYEDIPngExdltTFMb-dmKO5rfejy7M3oHAvmKlpTY8pYinUnQ0C2cGVNjFG0k9yLSjHjC4uOony32LbEkWTGST9fPprrY3Sn6oT8beOaRaQf'
band_key = 'AAAya6jGF4MUx5TXLm7eSun8'

stock_check = int(input("""What stock would you like to check?
                    1. Samsung 2. LG 3. SK 4. ALL
                    Please enter the number: """))         

send = int(input("""How would you like to check stock information?
             1. Band 2. file 3. Terminal
             Please enter the number: """))             

price_list = []
stock_codes = ['005930', '003550', '017670']
stock_names = ['삼성전자', 'LG', 'SK']



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
            return f"주식 가격을 찾을 수 없습니다."
    else:
        return f"오류 발생: {response.status_code}"

if 1 <= stock_check <= len(stock_codes):    
    stock_code = stock_codes[stock_check - 1]
    stock_name = stock_names[stock_check - 1]
    price = get_stock_price(stock_code) 

elif stock_check == 4:
    for i in range(3):
        stock_code = stock_codes[i]
        stock_name = stock_names[i]
        price = get_stock_price(stock_code)
        price_list.append(f"{stock_name} 주식 가격: {price}")

else:
    print('Please choose a number from the options provided.')

if send == 1: 
    if stock_check == 4:
        send_to_Band(band_key, f"{price_list[:]}")

    else:
        send_to_Band(band_key, f"{stock_name} 주식 가격: {price}")
    

elif send == 2:
    home_dir = os.path.expanduser("~")
    desktop_path = os.path.join(home_dir, "Desktop")   
    stock = os.path.join(desktop_path, "price.txt")
    if stock_check == 4:
        with open(stock, "w") as f:
            f.write(f"{price_list[:]}")

    else:
        with open(stock, "w") as f:
            f.write(f"{stock_name} 주식 가격: {price}")

elif send == 3:
    if stock_check == 4:
        print(f"{price_list[:]}")

    else:
        print(f"{stock_name} 주식 가격: {price}")

else:
    print('Please choose a number from the options provided.')

#chart_area > div.rate_info > div > p.no_today > em  금일 주식 가격
#chart_area > div.rate_info > table > tbody > tr:nth-child(1) > td.first > em   전일
#chart_area > div.rate_info > table > tbody > tr:nth-child(2) > td.first > em   시가