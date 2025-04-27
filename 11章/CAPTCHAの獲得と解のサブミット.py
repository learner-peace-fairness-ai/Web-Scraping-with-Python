from io import BytesIO
import re

from PIL import Image
from PIL import ImageOps
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://pythonscraping.com/humans-only"
WAIT_SECONDS = 10


def clean_image(binary):
    with BytesIO(binary) as buf:
        with Image.open(buf) as img:
            img.load()
            # しきい値を基準に色を白か黒にする
            img = img.point(lambda x: 0 if x < 143 else 255)
            # 画像を枠線で囲む
            return ImageOps.expand(img, border=20, fill="white")


driver = webdriver.Edge()
wait = WebDriverWait(driver, WAIT_SECONDS)
driver.get(URL)

# captcha画像を取得
CAPTCHA_IMAGE = "img[alt='captcha']"
captcha = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, CAPTCHA_IMAGE)))
captcha_binary = captcha.screenshot_as_png
img = clean_image(captcha_binary)

# OCR
text = pytesseract.image_to_string(img, config='--psm 7')
# 空白と改行を除去
text = re.sub(r"\s+", "", text)
print(f"Captcha solution attempt: {text}")

if len(text) == 4:
    # captchaの解答を入力
    CAPTCHA_FIELD = "input[name='captcha-170']"
    captcha_fld = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, CAPTCHA_FIELD)))
    captcha_fld.send_keys(text)
    
    # 名前を入力
    NAME_FIELD = "input[name='your-name']"
    name_fld = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, NAME_FIELD)))
    name_fld.send_keys("a")
    
    # メールアドレスを入力
    MAIL_ADDRESS_FIELD = "input[name='your-email']"
    mail_fld = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, MAIL_ADDRESS_FIELD)))
    mail_fld.send_keys("b@b.com")

    # テーマを入力
    SUBJECT_FIELD = "input[name='your-subject']"
    subject_fld = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, SUBJECT_FIELD)))
    subject_fld.send_keys("c")

    initial_url = driver.current_url

    # 送信
    SUBMIT_BUTTON = "form[aria-label='Contact form'] input[type='submit']"
    submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, SUBMIT_BUTTON)))
    submit.click()

    # ページの移動を待機
    wait.until(EC.url_changes(initial_url))

    print("Passed the CAPTCHA.")
else:
    print("There was a problem reading the CAPTCHA correctly!")
