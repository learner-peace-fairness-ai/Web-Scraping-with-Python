from pathlib import Path

from bs4 import BeautifulSoup
import requests

DOWNLOAD_DIRECTORY = Path('download')
PAGE_URL = 'https://www.pythonscraping.com'
BASE_URL = 'https://pythonscraping.com'


def get_absolute_url(base_url, source):
    HTTPS_AND_WWW = 'https://www.'
    HTTPS = 'https://'
    WWW = 'www.'

    if source.startswith(HTTPS_AND_WWW):
        url = source.replace(HTTPS_AND_WWW, HTTPS, 1)
    elif source.startswith(HTTPS):
        url = source
    elif source.startswith(WWW):
        url = source.replace(WWW, HTTPS, 1)
    else:
        url = f'{base_url}/{source}'
    
    if BASE_URL in url:
        return url
    else:
        None


def get_download_path(base_url, absolute_url, download_directory):
    path = absolute_url.replace(base_url, '')
    return download_directory / path


response = requests.get(PAGE_URL)
response.raise_for_status()
html = response.text
soup = BeautifulSoup(html, 'html.parser')
download_list = soup.find_all(src=True)

for download in download_list:
    file_url = get_absolute_url(BASE_URL, download['src'])
    if file_url is None:
        continue

    print(file_url)
    new_file = Path(get_download_path(BASE_URL, file_url, DOWNLOAD_DIRECTORY))
    
    # ダウンロード
    DOWNLOAD_DIRECTORY.mkdir(exist_ok=True)
    # download_file = requests.get(file_url)
    # with open(new_file, 'wb') as fw:
    #     for chunk in download_file.iter_content(chunk_size=100000):
    #         fw.write(chunk)
