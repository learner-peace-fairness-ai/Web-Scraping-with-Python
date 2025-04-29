from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://pythonscraping.com/pages/itsatrap.html"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)
    links = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "a")))
    for link in links:
        if not link.is_displayed():
            print(f"The link {link.get_attribute("href")} is a trap")

    fields = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "input")))
    for field in fields:
        if not field.is_displayed():
            print(f"Do not change value of {field.get_attribute("name")}")
