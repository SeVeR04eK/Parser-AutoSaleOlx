import requests
import html
from bs4 import BeautifulSoup
from typing import Generator, Dict, Any
from time import sleep
import os

#Loading variables from .env
from dotenv import load_dotenv
#import os

load_dotenv()
API_URL = os.getenv("SHOP_API_URL")
IMG_URL = os.getenv("SHOP_IMG_URL")

class Parser:
    url_base = API_URL

    @classmethod
    def get_json(cls, from_itemid, to_itemid) -> Generator[Dict[str, Any], None, None]:
        # Getting JSON
        for i in range(from_itemid, to_itemid + 1):
            url_ = cls.url_base + str(i)
            response = requests.get(url_)
            yield response.json()

    @staticmethod
    def save_image(img_url, folder="foto", filename="foto1.png"):
        os.makedirs(folder, exist_ok=True)

        save_path = os.path.join(folder, filename)

        if os.path.exists(save_path):
            os.remove(save_path)

        response = requests.get(img_url)
        with open(save_path, "wb") as f:
            f.write(response.content)
            sleep(7)


    @staticmethod
    def get_data(from_itemid, to_itemid):
        for data in Parser.get_json(from_itemid, to_itemid):
            if data["pages"] == 0:
                continue
            else:
                sleep(3)
                #Saving data in variables
                name = data["list"][0]["name"]
                img_base = IMG_URL+data["list"][0]["main_image_filename"]
                Parser.save_image(img_base)

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
                my_price = str(my_price).replace(".", ",")
                price = my_price

                yield name, description, my_price

# def main():
#     parser = Parser()
#     for item in parser.get_data(2000, 10000):
#         print(item[0],"\n")
#
# main()


