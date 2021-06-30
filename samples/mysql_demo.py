#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/23 10:54
# @Author : 杜云慧
# @Site : 
# @File : mysql_demo.py
# @Software: PyCharm

import pymysql

connect = pymysql.connect(host="",
                          port = 3306,
                          user='',
                          password='',
                          database='',
                          charset='utf-8')

cur = connect.cursor()
cur.execute('select * from case_step_info;')
print(cur.fetchone())