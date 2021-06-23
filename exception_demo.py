#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/17 17:08
# @Author : 杜云慧
# @Site : 
# @File : exception_demo.py
# @Software: PyCharm

import requests
from requests.exceptions import RequestException

# res =  requests.get(url = 'http://google.com.hk/')
# print(res.status_code)

try:

    num_list = [1, 2, 3, 4, 5]
    print(num_list[6])
except IndexError as e:
    print('索引错误')
except Exception as e:
    print('系统错误')  # 已知可能会发生的异常写前面，不确定原因的写在最后

print('hello')
