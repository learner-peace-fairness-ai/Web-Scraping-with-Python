from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://pythonscraping.com/pages/javascript/redirectDemo1.html"
WAIT_SECONDS = 10

options = Options()
options.add_argument('--headless')

with webdriver.Edge(options=options) as driver:
    driver.get(URL)
    initial_url = driver.current_url
    WebDriverWait(driver, WAIT_SECONDS).until(EC.url_changes(initial_url))
    print(driver.page_source)
