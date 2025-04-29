from selenium import webdriver

URL = "https://pythonscraping.com"

with webdriver.Edge() as driver:
    driver.get(URL)
    print(driver.get_cookies())
