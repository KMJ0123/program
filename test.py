#20244043 김민주
print("20244043 김민주")

import os

home_dir = os.path.expanduser("~")
print(home_dir)
desktop_path = os.path.join(home_dir, "Desktop")  
print(desktop_path)
stock = os.path.join(desktop_path, "price.txt")
print(stock)




