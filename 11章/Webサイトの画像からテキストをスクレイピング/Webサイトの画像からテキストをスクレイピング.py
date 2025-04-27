from io import BytesIO
import time

from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://www.amazon.co.jp/%E9%8A%80%E6%B2%B3%E9%89%84%E9%81%93%E3%81%AE%E5%A4%9C-%E5%AE%AE%E6%B2%A2-%E8%B3%A2%E6%B2%BB-ebook/dp/B01EUC17SW/"
WAIT_SECONDS = 10
GENTLEMANLY_WAIT_SECONDS = 1

with webdriver.Edge() as driver:
    wait = WebDriverWait(driver, WAIT_SECONDS)

    driver.get(URL)
    time.sleep(GENTLEMANLY_WAIT_SECONDS)

    SAMPLE_BUTTON = "ebooksReadSampleButton-announce"
    sample_btn = wait.until(EC.element_to_be_clickable((By.ID, SAMPLE_BUTTON)))
    sample_btn.click()
    time.sleep(GENTLEMANLY_WAIT_SECONDS)

    # サンプルのフレームに移動
    SAMPLE_FRAME = "litb-read-frame"
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, SAMPLE_FRAME)))
    time.sleep(GENTLEMANLY_WAIT_SECONDS)

    while True:
        # サンプルを読み終えたら終了
        NEXT_PAGE_ICON = "kr-chevron-left"
        exists_next_page_icon = bool(driver.find_elements(By.ID, NEXT_PAGE_ICON))
        if not exists_next_page_icon:
            break

        # 画像を取得
        SAMPLE_VIEW = "kr-renderer"
        sample_view = wait.until(EC.visibility_of_element_located((By.ID, SAMPLE_VIEW)))
        sample_page = sample_view.screenshot_as_png

        # 画像をOCR
        with BytesIO(sample_page) as buf:
            with Image.open(buf) as img:
                img.load()
                text = pytesseract.image_to_string(img, lang="jpn")
                print(text)

        # 次のページへ移動
        old_text = sample_view.text
        next_page_icon = wait.until(EC.element_to_be_clickable((By.ID, NEXT_PAGE_ICON)))
        next_page_icon.click()
        # ページが切り替わるまで待機
        wait.until(lambda d: sample_view.text != old_text)
        time.sleep(GENTLEMANLY_WAIT_SECONDS)
