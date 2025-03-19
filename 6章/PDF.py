from io import BytesIO

from PyPDF2 import PdfReader
import requests

def read_PDF(pdf_file):
    text_contents = []
    reader = PdfReader(pdf_file)
    for page in reader.pages:
        text_contents.append(page.extract_text())
    return '\n'.join(text_contents)


res = requests.get('https://pythonscraping.com/pages/warandpeace/chapter1.pdf')
with BytesIO(res.content) as buffer:
    text = read_PDF(buffer)
print(text)
