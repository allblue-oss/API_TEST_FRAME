#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/15 17:02
# @Author : 杜云慧
# @Site : 
# @File : requests_demo.py
# @Software: PyCharm

import requests

host = 'https://api.weixin.qq.com'
# 获取token
params = {
    'grant_type':'client_credential',
    'appid':'wx55614004f367f8ca',
    'secret':'65515b46dd758dfdb09420bb7db2c67f'
}

res01 = requests.get(url= host+'cgi-bin/token',params=params)
print(res01.json())