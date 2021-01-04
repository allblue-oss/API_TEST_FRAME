#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/4 15:13
# @Author : 杜云慧
# @Site : 
# @File : re_demo.py
# @Software: PyCharm

'''re模块'''

import re

# newdream

str1 = 'newdream,come on!'
pattrrn = re.compile(r'newdream')
result1 = re.match(pattrrn,str1)  # 匹配以什么开头
print(result1.string)
print(result1.re)
print(result1.pos)
print(result1.endpos)















