from selenium import webdriver

URL = "https://www.pythonscraping.com/"

with webdriver.Edge() as driver:
    FILENAME = "pythonscraping.png"

    driver.get(URL)
    driver.save_screenshot(FILENAME)
