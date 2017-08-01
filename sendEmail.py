#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器  服务器地址:POP3服务器: pop.163.com  端口：110 SMTP服务器: smtp.163.com 端口：25  IMAP服务器: imap.163.com
mail_user = "zhouchatian@163.com"  # 用户名
mail_pass = "xxx"  # 口令 要在163设置中设置，不是登录密码

sender = 'zhouchatian@163.com'
receivers = ['zhouchatian@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("测试邮件", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    # smtpObj = smtplib.SMTP('localhost') #本地有邮箱
    # smtpObj.sendmail(sender, receivers, message.as_string())

    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")