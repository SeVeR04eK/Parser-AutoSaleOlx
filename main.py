import requests
import html
from bs4 import BeautifulSoup

#Getting JSON
url = "https://www.kamille.pl/webapi/front/pl_PL/products/PLN/list/3801"
response = requests.get(url)
data = response.json()

#Saving data in variables
name = data["list"][0]["name"]
img = "https://www.kamille.pl/userdata/public/gfx/"+data["list"][0]["main_image_filename"]

#Desc
raw = data["list"][0]["description"]
#Cleaning HTML tags
decoded = html.unescape(raw)
soup = BeautifulSoup(decoded, "html.parser")

description = soup.get_text(separator = "", strip=True)

price_origin = float(data["list"][0]["price"]["gross"]["base"].replace(" zł", "").replace(",", "."))
price_origin_net = float(data["list"][0]["price"]["net"]["base"].replace(" zł", "").replace(",", "."))

#My price
middle_price = (price_origin + price_origin_net) / 2
my_price = round((price_origin + middle_price) / 2, 2)

