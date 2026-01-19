from parser import Parser
from auto_sale import init_driver, open_olx, post_ad
from time import sleep
from random import randint

def main():
    parser = Parser()
    batch_size = 20
    items = parser.get_data(3184, 3185)

    while True:
        driver, wait = init_driver()

        try:
            for _ in range(batch_size):
                try:
                    item = next(items)
                except StopIteration:
                    return  #end of the products

                try:
                    open_olx(driver)
                    post_ad(driver, wait, item[0], item[1], item[2])
                except Exception as e:
                    print("Error during posting:", e)
                    continue  #next product

                sleep(randint(20, 70))

        finally:
            driver.quit()

if __name__ == "__main__":
    main()

