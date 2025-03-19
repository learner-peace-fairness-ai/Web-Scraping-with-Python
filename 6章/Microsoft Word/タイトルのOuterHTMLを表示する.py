from io import BytesIO

from bs4 import BeautifulSoup
from docx import Document
import requests

res = requests.get('https://pythonscraping.com/pages/AWordDocument.docx')
with BytesIO(res.content) as buffer:
    doc = Document(buffer)

    for para in doc.paragraphs:
        if para.style.name == 'Heading 1':
            xml_str = para._element.xml
            soup = BeautifulSoup(xml_str, 'lxml-xml')
            
            title_tags = soup.find_all('w:t')
            for title_tag in title_tags:
                print(title_tag)
