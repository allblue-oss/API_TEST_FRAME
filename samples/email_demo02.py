#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/21 17:17
# @Author : 杜云慧
# @Site : 
# @File : email_demo02.py
# @Software: PyCharm

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

msg = MIMEMultipart()
msg.attach(MIMEText('<h3 align="center">自动化测试报告</h3>', 'html', 'utf-8'))
msg['from'] = '785045798@qq.com'
msg['to'] = '785045798@qq.com'
msg['Cc'] = '785045798@qq.com'  # 抄送
msg['subject'] = '邮件主题'

html_path = os.path.join( os.path.dirname(__file__),'..','test_reports/P1P2接口自动化测试报告V1.0/P1P2接口自动化测试报告V1.0.html')

attach_file = MIMEText( open(html_path,'rb').read(),'base64','utf-8')
attach_file['Content_Type'] = 'application/octet-stream'
attach_file['Content_Dispositon'] = 'attachment; filename = "newdream.txt"'
msg.attach(attach_file)

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(user='785045798@qq.com', password='zbrigdqplbvibfij')
smtp.sendmail('785045798@qq.com', ['785045798@qq.com'], msg.as_string())
