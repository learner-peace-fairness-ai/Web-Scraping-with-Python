from selenium import webdriver

URL = "https://en.wikipedia.org/wiki/Monty_Python"

with webdriver.Edge() as driver:
    driver.get(URL)
    assert "Monty Python" in driver.title
