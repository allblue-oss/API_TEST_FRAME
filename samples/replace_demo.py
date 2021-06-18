#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/5 15:48
# @Author : 杜云慧
# @Site : 
# @File : replace_demo.py
# @Software: PyCharm

import re
import ast
import requests

temp_variables = {"token": "123456"}

params = '{"access_token":${token}}'  # 考虑一个以上的情况
value = re.findall('\\${\w+}', params)[0]
print(value)
params = params.replace(value, temp_variables.get(value[2:-1]))

print(params)


temp_variables = {"token":"123456","number":"123","age":"66"}

str1 = '{"access_token":${token},${age}==>${number}}'
for v in re.findall('\\${\w+}', str1):
    str1 = str1.replace(v,temp_variables.get(v[2:-1]))
print(str1)

str1 = re.sub('\\${\w+}', r'123456',str1)
print(str1)






# requests.get(url = "/cgi-bin/tags/delete",
#              params=ast.literal_eval(params))
