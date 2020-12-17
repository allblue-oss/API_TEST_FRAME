#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/17 14:10
# @Author : 杜云慧
# @Site : 
# @File : requests_demo02.py
# @Software: PyCharm

import requests

response = requests.get('http://www.hnxmxit.com/')
# print(response.json())
# response.encoding = 'utf-8'
# print(response.text)

# print(response.headers)

# print(response.content.decode("utf-8"))

print(response.apparent_encoding)
response.encoding =response.apparent_encoding
print(response.text)
