# coding=utf-8
# @author = zhangyang
# date: 2020-03-03

# 实现邮件发送相关的功能
import smtplib
# 定义邮件的格式
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

# 第三方 SMTP 服务
mail_host = 'smtp.163.com'
mail_user = 'xxx@163.com'
mail_pass = 'xxxx'

# 初始化发件人和收件人
mail_sender = 'xxx@163.com'
mail_port = '465'
mail_receivers = ['xxx@163.com','xxx@qq.com']


# 邮件内容相关的设置
message = MIMEText('来自 zhangyang 的测试邮件',"plain",'utf-8')
# 设置图片


# 设置邮件的收发件人
message['From'] = mail_sender
message['To'] = ','.join(mail_receivers)
message['Subject'] = Header("Python test mail","utf-8")


# 尝试发送
try:
    smtpObj = smtplib.SMTP_SSL(mail_host,mail_port)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(mail_sender,mail_receivers,message.as_string())
    print('Success')
except smtplib.SMTPException:
    print('Failed')
