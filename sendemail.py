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

fp=open("E:\sublime\python\day13\计算器.html","r"，encoding="utf-8")
msg=email.message_from_file(fp)
fp.close()
for par in msg.walk():
    if not par.is_multipart():
        connect=par.get_payload(decode=True).decode('utf-8')

def send_email():
    msg=MIMEText(connect,'html')
    msg["Subject"]=Header(subject,'utf-8')
    msg["From"]=msg_from
    msg["To"]=to

    #发送邮件            服务器地址
    ss=smtplib.SMTP_SSL("smtp.qq.com")
    ss.connect("smtp.qq.com")
    ss.login(msg_from,pwd)
    #            发送方
    ss.sendmail(msg_from,to,msg.as_string())
    print("邮件已发送")
    ss.quit()
    print("系统结束")
send_email()
