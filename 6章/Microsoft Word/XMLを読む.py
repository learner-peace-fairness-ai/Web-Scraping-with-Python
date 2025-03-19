from io import BytesIO

from docx import Document
import requests

res = requests.get('https://pythonscraping.com/pages/AWordDocument.docx')
with BytesIO(res.content) as buffer:
    doc = Document(buffer)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
print('\n'.join(full_text))
