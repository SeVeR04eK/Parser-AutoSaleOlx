from stealth_driver import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = get_driver()
wait = WebDriverWait(driver, 20)
def open_olx():
    driver.get("https://www.olx.pl/adding/")
def post_ad():
    # ---------- Title ----------
    title_input = wait.until(
        EC.element_to_be_clickable((By.NAME, "title"))
    )
    title_input.send_keys("Czajnik elektryczny kamille")

    # ---------- Description ----------
    desc = wait.until(
        EC.presence_of_element_located((By.ID, "description"))
    )
    desc.send_keys("Telefon w bardzo dobrym stanie, działa perfekcyjnie.")

    # ---------- Condition (Stan) ----------
    fields = WebDriverWait(driver, 20).until(
        lambda d: d.find_elements(By.CSS_SELECTOR, "input.n-textinput-input[role='combobox']")
                  if len(d.find_elements(By.CSS_SELECTOR, "input.n-textinput-input[role='combobox']")) >= 2
                  else False
    )

    fields[1].click()

    option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@role='option' and contains(., 'Nowe')]")
        )
    )
    option.click()

    # ---------- Price ----------
    price = wait.until(
        EC.element_to_be_clickable((By.NAME, "parameters.price.price"))
    )
    price.send_keys("1200")

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

    driver.find_element(
        By.XPATH, "//input[@aria-label='POCZTA package size L']"
    ).click()

    # ---------- Courier delivery (radio buttons) ----------
    radios = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "input[type='radio'][data-testid^='radio-']")
        )
    )
    driver.execute_script("arguments[0].click();", radios[1])

    # ---------- Image upload ----------
    photo_input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
    )
    photo_input.send_keys(
        r"C:\Programming\Projects (mixed)\Parser-AutoPostOLX\foto\foto1.png"
    )

    # Keep browser open for manual review
    wait.until(lambda d: False)

    # submit_btn = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-button']")
    # submit_btn.click()