# -*- coding:utf-8 -*-

import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'isyishantao@163.com'
password = 'yishantao0825'  # 开启邮箱服务后，设置的客户端授权密码
receivers = ['769338809@qq.com']

message = MIMEMultipart('related')
message['From'] = sender
message['To'] = receivers[0]
subject = 'Python邮件测试'
message['Subject'] = Header(subject, 'utf-8')

messageAlternative = MIMEMultipart('alternative')
message.attach(messageAlternative)

mail_msg = """
<html>
<body>
<p>Python邮件发送测试</p>
<p><a href="https://www.python.org">Python官方网站</a></p>
<p>图片演示：</p>
<p><img src="cid:image1" alt="image1"></p>
</body>
</html>
"""
messageAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))

fp = open('book.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片ID，在HTML文本中引用
msgImage.add_header('Content-ID', '<image1>')
message.attach(msgImage)

try:
    # 使用非本地服务器，需要建立ssl连接
    smtp_object = smtplib.SMTP_SSL('smtp.163.com', 465)
    smtp_object.login(sender, password)
    smtp_object.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功！')
except smtplib.SMTPException as e:
    print('无法发送邮件case:%s' % e)
