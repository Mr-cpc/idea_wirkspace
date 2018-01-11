import smtplib
from email.mime.text import MIMEText

__user='2281085631@qq.com'
__pwd = 'qbfngfhuclbudjbj'
__to = '615706431@qq.com'



def inform(content:str,title:str):
    msg = MIMEText(content)
    msg['Subject'] = title
    msg['From']  = __user
    msg['To'] = __to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com",465)
        s.login(__user,__pwd)
        s.sendmail(__user,__to,msg.as_string())
        s.quit()
        print("send advice success!")
    except smtplib.SMTPException as e:
        print("Failed,%s"%e)

inform('ceshi','测试哦')