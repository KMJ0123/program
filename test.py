import urllib.request, time

def get_price():
    page = urllib.request.urlopen(" http://cs.sch.ac.kr/prices-loyalty.py")
    text = page.read().decode("utf8")

    if price_now == ('Y'):
        where = text.find(">$")
        start_of_price = where + 2
        end_of_price = start_of_price + 4
        price = float(text[start_of_price : end_of_price])

        return float(text[start_of_price: end_of_price])
        

    else:
        where = text.find(">$")
        start_of_price = where + 2
        end_of_price = start_of_price + 4
        price = float(text[start_of_price : end_of_price])
        
        where = text.find("Price on")
        start_of_price = where + 9
        end_of_price = start_of_price + 24
        date = text[start_of_price : end_of_price]
        
        return price, date


price_now = input('Do you want to see the price now(Y/N)?')

if price_now == "Y":
    print(price_now)
else:
    price, date = get_price()
    print(get_price)