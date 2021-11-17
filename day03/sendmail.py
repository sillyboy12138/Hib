import smtplib
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header

msg_from = '3072791869@qq.com'
pwd = 'sentiolwdugldgci'
to = '3072791869@qq.com'
subject = 'python test'

def send():
    msg=MIMEMultipart()
    text=MIMEText('HKR系统测试报告')
    msg.attach(text)
    msg['Subject']=Header(subject,'utf-8')
    msg['From']=msg_from
    msg['To']=to
    connect=MIMEApplication(open(r'E:\自动化\day03\HKR.html','rb').read())

    connect.add_header('Content-Disposition', 'attachment', filename='HKR.html')
    msg.attach(connect)

    ss=smtplib.SMTP_SSL('smtp.qq.com')
    ss.login(msg_from,pwd)
    ss.sendmail(msg_from,to,msg.as_string())
    print("邮件已发送！")
    ss.quit()
send()