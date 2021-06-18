#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/6 16:27
# @Author : 杜云慧
# @Site : 
# @File : checkdemo.py
# @Software: PyCharm

import re
import ast
# 正则匹配测试

# 实际结果
str1 = '{"access_token":"40_MHpY90YEGA7efoRMvZ7zjMA34gD3rAWWCkmbIVlNd_lEEBqrB3b_OIV3V_gEOnYiPQrctVjDIlftJK85on3ZicfxQL7llg43fBwwXw4IgpE54mOP26brt0Rug2mPbSk6m12xcimY766yZ1P0CDQiADAHIV"}'

# 期望结果
str2 = '{"access_token":"(.+?)","expires_in":(.+?)}'

if re.findall(str2,str1):
    print(True)
else:
    print(False)

# 是否包含 json key
jsondata1 = ast.literal_eval(str1)
str2 = 'access_token,expires_in'
check_key_list = str2.split(',')
for check_key in check_key_list:
    result = True
    if check_key in jsondata1.keys():
        result = True
    else:
        result=False
    if not result:
        break
print(result)
# print('access_token' in jsondata1.keys())


# 键值对正常的情况
str2 = '{"expires_in":7200}'

for v in ast.literal_eval(str2).items():
    if v in jsondata1.items():
        print(True)
    else:
        print(False)




