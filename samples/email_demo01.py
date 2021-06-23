#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/21 16:09
# @Author : 杜云慧
# @Site : 
# @File : email_demo01.py
# @Software: PyCharm

import smtplib
from email.mime.text import MIMEText

body_str = """
<h3 align="center">自动化测试报告</h3>
<table border="2" align="center" width="50%",height="400">
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
<tr><td></td><td></td><td></td><td></td></tr>
</table>
"""

msg = MIMEText(body_str, 'html', 'utf-8')

msg['from'] = '785045798@qq.com'
msg['to'] = '785045798@qq.com'
msg['Cc'] = '785045798@qq.com'  # 抄送
msg['subject'] = '邮件主题'

smtp = smtplib.SMTP()
smtp.connect('smtp.qq.com')
smtp.login(user='785045798@qq.com', password='zbrigdqplbvibfij')
smtp.sendmail('785045798@qq.com', ['785045798@qq.com'], msg.as_string())
