from email.message import EmailMessage
from smtplib import SMTP
import sys

from bs4 import BeautifulSoup
import requests
import time

URL = 'https://isitchristmas.com/'
WAIT_SEC = 3600
MAIL_ACCOUNT = sys.argv[1]
TO_ADDRESS   = sys.argv[2]
APP_PASWORD  = sys.argv[3]


def send_mail(subject, body):
    msg = EmailMessage()
    msg['From'] = MAIL_ACCOUNT
    msg['To']   = TO_ADDRESS
    msg['Subject'] = subject
    msg.set_content(body)

    with SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(MAIL_ACCOUNT, APP_PASWORD)
        server.send_message(msg)


def is_christmas():
    res = requests.get(URL)
    res.raise_for_status()
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup.select_one('#answer').get('title') == 'はい'


while not is_christmas():
    print('It is not Christmas yes.')
    time.sleep(WAIT_SEC)

send_mail("It's Christmas!", f'According to {URL}, it is Christmas!')
