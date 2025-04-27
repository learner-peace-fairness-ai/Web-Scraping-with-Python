from PIL import Image
from PIL import ImageFilter

with Image.open("cat.png") as img:
    blurry_img = img.filter(ImageFilter.GaussianBlur)
    blurry_img.save("cat_blurred.png")
    blurry_img.show()
