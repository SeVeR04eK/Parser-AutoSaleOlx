from stealth_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from random import randint

# driver
def init_driver():
    driver = get_driver()
    wait = WebDriverWait(driver, 20)
    return driver, wait

def open_olx(driver):
    driver.get("https://www.olx.pl/adding/")

def post_ad(driver, wait, name_in, desc_in, price_in):
    #Old ad error fix
    try:
        new_btn = WebDriverWait(driver, 7).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//button[.//span[contains(text(), 'Nie, zaczynam od nowa')]]"
            ))
        )
        new_btn.click()
    except:
        pass

    # ---------- Title ----------
    title_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "title"))
    )
    title_input.send_keys(name_in)
    print("Step 1: title")

    # ---------- Description ----------
    desc = wait.until(
        EC.presence_of_element_located((By.ID, "description"))
    )
    desc.send_keys(desc_in)
    print("Step 2: description")

    # ---------- Condition (Stan) ----------
    try:
        fields = WebDriverWait(driver, 20).until(
            lambda d: d.find_elements(By.CSS_SELECTOR, "input.n-textinput-input[role='combobox']")
        )

        if len(fields) >= 2:
            target = fields[1]
        else:
            target = fields[0]

        driver.execute_script("arguments[0].click();", target)

        option = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@role='option' and contains(., 'Nowe')]")
            )
        )
        driver.execute_script("arguments[0].click();", option)
    except:
        pass

    # print("Step 3: New")
    # ---------- Price ----------
    price = wait.until(
        EC.element_to_be_clickable((By.NAME, "parameters.price.price"))
    )
    price.send_keys(price_in)
    print("Step 4: Price")

    # ---------- Delivery: expand size L ----------
    toggle = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[@data-testid='band-L-toggle']/ancestor::header")
        )
    )
    toggle.click()

    # ---------- Delivery: select all carriers ----------
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@aria-label='INPOST package size L']")
        )
    )

    driver.find_element(
        By.XPATH, "//input[@aria-label='INPOST package size L']"
    ).click()

    driver.find_element(
        By.XPATH, "//input[@aria-label='RUCH package size L']"
    ).click()

    # ---------- Courier delivery (radio buttons) ----------
    radios = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "input[type='radio'][data-testid^='radio-']")
        )
    )
    driver.execute_script("arguments[0].click();", radios[1])
    print("Step 5: delivery")
    # ---------- Image upload ----------
    photo_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
    )
    photo_input.send_keys(
        r"C:\Programming\Projects (mixed)\Parser-AutoPostOLX\foto\foto1.png"
    )
    print("Step 6: photo")

    sleep(randint(4, 10))
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-btn']")
    submit_btn.click()

    sleep(randint(5, 8))

# def main():
#     driver, wait = init_driver()
#     open_olx(driver)
#     name1 = "Czajnik wlwktryczny kamille 3l"
#     desc1 = "czajnik elektryczny 3l kamille dlugi opis bla bla test sory ol_x"
#     prise1 = "150"
#     post_ad(driver, wait, name1, desc1, prise1)
#
# main()