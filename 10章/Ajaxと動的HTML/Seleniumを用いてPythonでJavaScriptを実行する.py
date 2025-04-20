from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://pythonscraping.com/pages/javascript/ajaxDemo.html"
WAIT_SECONDS = 10

options = Options()
options.add_argument('--headless')

with webdriver.Edge(options=options) as driver:
    driver.get(URL)
    WebDriverWait(driver, WAIT_SECONDS).until(EC.presence_of_element_located((By.ID, "loadedButton")))
    text = driver.find_element(By.ID, "content").text
    print(text)
