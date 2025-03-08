import csv

from bs4 import BeautifulSoup
import requests


response = requests.get('https://en.wikipedia.org/wiki/Comparison_of_text_editors')
html = response.text
soup = BeautifulSoup(html, 'html.parser')

# 主たる比較表はページの最初の表
caption = soup.select_one('caption:contains("List of text editors")')
table = caption.parent
rows = table.find_all('tr')

with open('editors.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    for row in rows:
        csv_row = []
        for cell in row.select('td, th'):
            csv_row.append(cell.get_text())

        writer.writerow(csv_row)
