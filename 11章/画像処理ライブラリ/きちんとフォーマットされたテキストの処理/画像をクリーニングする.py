from PIL import Image
import pytesseract


def get_clean_file(file_path):
    with Image.open(file_path) as img:
        # 画像のしきい値を設定して返す
        return img.point(lambda x: 0 if x < 143 else 255)


# 元の画像のOCRをする
with Image.open("gradient_text.png") as img:
    print(f"元の画像: {pytesseract.image_to_string(img, lang='jpn')}")

# クリーニングした画像のOCRをする
with get_clean_file("gradient_text.png") as img:
    print(f"クリーニングした画像: {pytesseract.image_to_string(img, lang='jpn')}")
