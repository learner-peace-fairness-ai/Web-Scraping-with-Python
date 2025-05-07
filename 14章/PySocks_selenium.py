from selenium import webdriver
from selenium.webdriver.edge.options import Options

URL = "https://icanhazip.com/"

edge_options = Options()
edge_options.use_chromium = True
edge_options.add_argument("--proxy-server=socks5://127.0.0.1:9050")

with webdriver.Edge(options=edge_options) as driver:
    driver.get(URL)
    print(driver.page_source)
