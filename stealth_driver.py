import undetected_chromedriver as uc

def get_driver():
    options = uc.ChromeOptions()

    options.add_argument(r"--user-data-dir=C:\Programming\Projects (mixed)\Parser-AutoPostOLX\ChromeProfile")
    options.add_argument("--profile-directory=Default")

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-infobars")
    options.add_argument("--window-size=1280,800")

    # Ключевые флаги
    options.add_argument("--no-first-run")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--allow-profiles-outside-user-dir")
    options.add_argument("--enable-profile-shortcut-manager")

    driver = uc.Chrome(options=options)
    return driver