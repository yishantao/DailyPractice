# -*-coding:utf-8 -*-

import poplib
from email.parser import Parser
from parse_file import *

# 输入邮件地址、口令和POP3服务器地址
email = input('email_file:')
password = input('Password:')
pop3_server = input('POP3 server:')

# 连接到POP3服务器
server = poplib.POP3(pop3_server)
# 可以打开或关闭调试信息
server.set_debuglevel(1)
# 可选：输出POP3服务器的欢迎文字
print(server.getwelcome().decode('utf-8'))

# 身份认证
server.user(email)
server.pass_(password)

# stat()返回邮件数量和占用空间
print('Messages:%s. Size:%s' % server.stat())
# list()返回所有邮件的编号
resp, mails, octets = server.list()
# 可以查看返回的列表
print(mails)

# 获取最新一封邮件
index = len(mails)
resp, lines, octets = server.retr(index)

# lines存储了邮件原始文本的每一行
# 可以获得整个邮件的原始文本
msg_content = b'\r\n'.join(lines).decode('utf-8')
# 稍后解析邮件
msg = Parser().parsestr(msg_content)
print_info(msg)
# 可以根据邮件索引号直接从服务器删除邮件
# server.dele(index)
# 关闭连接
server.quit()
