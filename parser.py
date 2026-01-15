import requests
import html
from bs4 import BeautifulSoup
from typing import Generator, Dict, Any
from time import sleep

class Parser:
    url_base = "https://www.kamille.pl/webapi/front/pl_PL/products/PLN/list/"
    @classmethod
    def get_json(cls) -> Generator[Dict[str, Any], None, None]:
        # Getting JSON
        for i in range(1, 10001):
            url_ = cls.url_base + str(i)
            response = requests.get(url_)
            yield response.json()
    @staticmethod
    def get_data():
        for data in Parser.get_json():
            if data["pages"] == 0:
                continue
            else:
                sleep(3)
                #Saving data in variables
                name = data["list"][0]["name"]
                img = "https://www.kamille.pl/userdata/public/gfx/"+data["list"][0]["main_image_filename"]

                #Desc
                raw = data["list"][0]["description"]
                #Cleaning HTML tags
                decoded = html.unescape(raw)
                soup = BeautifulSoup(decoded, "html.parser")

                description = soup.get_text(separator = "", strip=True)

                price_origin = float(
                    data["list"][0]["price"]["gross"]["base"].replace(" zł", "").replace(",", ".")
                )
                price_origin_net = float(
                    data["list"][0]["price"]["net"]["base"].replace(" zł", "").replace(",", ".")
                )

                #My price
                middle_price = (price_origin + price_origin_net) / 2
                my_price = round((price_origin + middle_price) / 2, 2)

                yield name, img, description, my_price

def main():
    parser = Parser()
    for item in parser.get_data():
        print(item,"\n")
