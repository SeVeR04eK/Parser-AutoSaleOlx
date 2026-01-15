from stealth_driver import get_driver
import time

driver = get_driver()
driver.get("https://www.olx.pl/")
time.sleep(15)
driver.quit()