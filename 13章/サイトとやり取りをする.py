import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://pythonscraping.com/pages/files/form.html"
WAIT_SECONDS = 10
GENTELMANLY_WAIT_SECONDS = 1

with webdriver.Edge() as driver:
    INPUT_FIRST_NAME = "firstname"
    INPUT_LAST_NAME = "lastname"
    SUBMIT_BUTTON = "submit"
    BODY = "body"

    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)

    first_name_field = wait.until(
        EC.presence_of_element_located((By.NAME, INPUT_FIRST_NAME))
    )
    last_name_field = wait.until(
        EC.presence_of_element_located((By.NAME, INPUT_LAST_NAME))
    )
    submit_btn = wait.until(EC.element_to_be_clickable((By.ID, SUBMIT_BUTTON)))

    # 手法1
    first_name_field.send_keys("Ryan")
    last_name_field.send_keys("Mitchell")
    submit_btn.click()

    body = wait.until(EC.presence_of_element_located((By.TAG_NAME, BODY)))
    print(body.text)

    # 元のページに戻る
    driver.back()
    time.sleep(GENTELMANLY_WAIT_SECONDS)

    # フォームをリセット
    first_name_field = wait.until(
        EC.presence_of_element_located((By.NAME, INPUT_FIRST_NAME))
    )
    last_name_field = wait.until(
        EC.presence_of_element_located((By.NAME, INPUT_LAST_NAME))
    )
    submit_btn = wait.until(EC.element_to_be_clickable((By.ID, SUBMIT_BUTTON)))
    first_name_field.clear()
    last_name_field.clear()

    # 手法2
    action_chains = ActionChains(driver)
    action_chains.click(first_name_field).send_keys("Ryan")
    action_chains.click(last_name_field).send_keys("Mitchell")
    action_chains.click(submit_btn)
    action_chains.perform()

    body = wait.until(EC.presence_of_element_located((By.TAG_NAME, BODY)))
    print(body.text)
