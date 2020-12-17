#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/15 17:02
# @Author : 杜云慧
# @Site : 
# @File : requests_demo.py
# @Software: PyCharm

import requests


host = 'https://api.weixin.qq.com'
session = requests.session()
# 获取token
params = {
    'grant_type': 'client_credential',
    'appid': 'wxdd1e072d49643bf0',
    'secret': 'c6868a07c562c932292eabdccda250a6'
}

res01 = session.get(url=host + '/cgi-bin/token', params=params)

# token_id = res01.json()['access_token']
print(res01.json())
