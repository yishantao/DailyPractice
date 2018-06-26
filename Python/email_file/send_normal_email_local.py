# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'isyishantao@163.com'
receivers = ['769338809@qq.com']

# 三个参数，第一个为文本内容，第二个plain设置文本格式，第三个utf-8设置编码
message = MIMEText('Python邮件发送测试', 'plain', 'utf-8')
message['From'] = sender
message['To'] = receivers[0]

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtp_object = smtplib.SMTP_SSL('localhost')
    smtp_object.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功！')
except smtplib.SMTPException as e:
    print('无法发送邮件case:%s' % e)
