from email.message import EmailMessage
from smtplib import SMTP
import sys

MAIL_ACCOUNT = sys.argv[1]
TO_ADDRESS   = sys.argv[2]
APP_PASWORD  = sys.argv[3]

msg = EmailMessage()
msg['From'] = MAIL_ACCOUNT
msg['To']   = TO_ADDRESS
msg['Subject'] = 'An Email Alert'
msg.set_content('The body of the email is here')

with SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(MAIL_ACCOUNT, APP_PASWORD)
    server.send_message(msg)
