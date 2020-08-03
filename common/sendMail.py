import os,sys
import smtplib
import configparser
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import setting
from common.newReport import new_report

def send_mail(file_name):
    """发送邮件
    :param file_name
    :return 成功：打印发送成功；失败：返回失败信息
    """
    con = configparser.ConfigParser()
    con.read(setting.TEST_CONFIG, encoding="utf-8")
    f=open(file_name,'rb')
    mail_body = f.read()
    f.close()
    #发送附件
    report = new_report(setting.TEST_REPOST)
    sendfile = open(report,'rb').read()
    #读取config.ini配置
    HOST = con.get("email_user","HOST_SERVER")
    SENDER = con.get("email_user","FROM")
    RECEIVE = con.get("email_user","TO")
    USER = con.get("email_user","user")
    PWD = con.get("email_user","password")
    SUBJECT = con.get("email_user","SUBJECT")
    SWITCH = con.get("email_user","SWITCH")
    if SWITCH == "OFF":
        print("邮件发送开关关闭，不发送邮件！")
    elif SWITCH == "ON":
        #创建附件实例
        msg = MIMEMultipart()
        # 构造附件实例
        att = MIMEText(sendfile,"base64","utf-8")
        att["Content-Type"] = 'application/octet-stream'
        att.add_header("Content-Disposition","attachment",filename=("gbk","",report.split("\\")[-1]))
        msg.attach(att)

        msgtext = MIMEText(mail_body,"html","utf-8")
        msg.attach(msgtext)
        msg["Subject"] = SUBJECT
        msg["from"] = SENDER
        msg["to"] = RECEIVE

        try:
            server = smtplib.SMTP(HOST)
            server.connect(HOST)
            server.starttls()
            server.login(USER,PWD)
            server.sendmail(SENDER,RECEIVE,msg.as_string())
            server.quit()
            print("邮件发送成功！")
        except Exception as e:
            print("邮件发送失败，原因是%s" %e)
