from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://pythonscraping.com/pages/javascript/draggableDemo.html"
WAIT_SECONDS = 10

with webdriver.Edge() as driver:
    DIV_MESSAGE = "message"
    DIV_DRAGGABLE = "draggable"
    DIV_TARGET = "div2"

    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)

    message_tag = wait.until(EC.presence_of_element_located((By.ID, DIV_MESSAGE)))
    text = message_tag.text
    print(text)

    elem = wait.until(EC.visibility_of_element_located((By.ID, DIV_DRAGGABLE)))
    target = wait.until(EC.visibility_of_element_located((By.ID, DIV_TARGET)))
    action_chains = ActionChains(driver)
    action_chains.drag_and_drop(elem, target)
    action_chains.perform()

    wait.until(lambda d: message_tag.text != text)
    print(message_tag.text)
