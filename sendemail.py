import email
import smtplib
import time
from email.mime.text import MIMEText
# from HTMLTestRunner import HTMLTestRunner
from email.mime.multipart import MIMEMultipart
from email.header import Header
# import unittest
#发送方
msg_from='3072791869@qq.com'
pwd='sentiolwdugldgci'
to='3072791869@qq.com'
t=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
subject='python repetion test' +t

def send_email():
    msg=MIMEMultipart()
    part_text=MIMEText('来自郭宏博的运算测试报告')
    msg.attach(part_text)
    msg["Subject"]=Header(subject,'utf-8')
    msg["From"]=msg_from
    msg["To"]=to
    connect = MIMEApplication(open(r'E:\sublime\python\day13\计算器.html', 'rb').read())
    connect.add_header('Content-Disposition', 'attachment', filename='运算测试')
    msg.attach(connect)
    #发送邮件            服务器地址
    ss=smtplib.SMTP_SSL("smtp.qq.com")
    ss.login(msg_from,pwd)
    #            发送方
    ss.sendmail(msg_from,to,msg.as_string())
    print("邮件已发送")
    ss.quit()
    print("系统结束")
send_email()
