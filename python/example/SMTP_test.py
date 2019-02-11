# FileName  : SMTP_test.py
# Author    : Lee, Jehyeon

import smtplib
from email.mime.text import MIMEText

'''
Google, MS 등 많은 회사들이 SMTP 서버를 사용할 수 있도록 오픈하고 있기 때문에
이들 SMTP 서버를 사용해서 메일을 발송할 수 있다.

SMTP 서버의 Encryption 방식에 따라 TTL 혹은 SSL을 사용한다.
TLS를 사용하는 경우 smtplib.SMTP(), SSL을 사용하는 경우 smtplib.SMTP_SSL()을 사용한다.
보통 TLS는 587, SSL은 465 포트를 사용한다.

Mail Provider                       SMTP Server, port
Live                                smtp.live.com, 587
Gmail                               smtp.gmail.com, 587
'''
print("Start")
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()     # say Hello
smtp.starttls() # When use TLS
print("Before Login")
smtp.login('********@gmail.com', 'password')
print("After Login")
msg = MIMEText('본문 텍스트 메시지')
msg['Subject'] = '테스트'
msg['To'] = '********@gmail.com'
smtp.sendmail('********@gmail.com', '********@gmail.com', msg.as_string())
print("ok")
smtp.quit()
print("finish")
