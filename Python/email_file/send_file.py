# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = 'isyishantao@163.com'
password = 'yishantao0825'  # 开启邮箱服务后，设置的客户端授权密码
receivers = ['769338809@qq.com']

# 创建一个带附件的实例
message = MIMEMultipart()
# message['From'] = Header('邮件测试', 'utf-8')
message['From'] = sender
# message['To'] = Header('测试', 'utf-8')
message['To'] = receivers[0]
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('Python邮件测试', 'plain', 'utf-8'))

# 构造附件1
att1 = MIMEText(open('text.txt', 'rb').read(), 'base64', 'utf-8')
att1['Content-Type'] = 'application/octet-stream'
# filename可以任意写，写什么名字，邮件中就显示什么名字
att1['Content-Disposition'] = 'attachment;filename="text.txt"'
message.attach(att1)

# 构造附件2
att2 = MIMEText(open('file.txt', 'rb').read(), 'base64', 'utf-8')
att2['Content-Type'] = 'application/octet-stream'
att2['Content-Disposition'] = 'attachment;filename="file.txt"'
message.attach(att2)

try:
    # 使用非本地服务器，需要建立ssl连接
    smtp_object = smtplib.SMTP_SSL('smtp.163.com', 465)
    smtp_object.login(sender, password)
    smtp_object.sendmail(sender, receivers, message.as_string())
    print('邮件发送成功！')
except smtplib.SMTPException as e:
    print('无法发送邮件case:%s' % e)
