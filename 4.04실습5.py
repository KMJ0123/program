#20244043 김민주
print('20244043 김민주')

import json
from urllib import request, parse
import time

token = 'ZQAAAYEDIPngExdltTFMb-dmKO5rfejy7M3oHAvmKlpTY8pYinUnQ0C2cGVNjFG0k9yLSjHjC4uOony32LbEkWTGST9fPprrY3Sn6oT8beOaRaQf'
band_key = 'AAAya6jGF4MUx5TXLm7eSun8'

def send_to_Band(bk, content, do_push=True):
    url = 'https://openapi.band.us/v2.2/band/post/create'
    req = request.Request(url)
    data = {'access_token': token, 'band_key': bk, 'content': content, 'do_push': do_push}
    post_data = parse.urlencode(data).encode('utf8')
    res = request.urlopen(req, post_data)
    print(f'전송완료,{content}')

def get_price():
    page = request.urlopen("http://cs.sch.ac.kr/prices-loyalty.py ")
    text = page.read().decode("utf8")
    where = text.find('>$')
    start_of_price = where + 2
    end_of_price = start_of_price + 4
    return float(text[start_of_price:end_of_price])

price_now = input("Do you want to see the price now(Y/N)?")
if price_now == "Y":
    msg = "Buy now!, price $" + str(get_price())
    send_to_Band(band_key, msg)

else:
    price = 99.99
    while price > 4.74:
        time.sleep(2)
        price = get_price()

    msg = "Buy!, price $" + str(price)
    send_to_Band(band_key, msg)