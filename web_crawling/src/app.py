_author_ = 'Ta-Seen Junaid'

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.ebay.com/itm/360-Universal-Car-Holder-Stand-Mount-Windshield-Bracket-For-Mobile-Cell-Phone/232952513663?hash=item363d0d447f:m:mpf0LDHRwIqn6T7IPzHhZ5g")

content = request.content

soup = BeautifulSoup(content, "html.parser")
element = soup.find("span",{"class":"notranslate", "itemprop":"price"})
string_price = element.text.strip()

only_price = string_price[4:]

price = float(only_price)

if price < 2:
    print("Price is reasonable, you can buy it at {}".format(only_price))
else:
    print("It is too high")






