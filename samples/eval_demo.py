#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/17 12:57
# @Author : 杜云慧
# @Site : 
# @File : eval_demo.py
# @Software: PyCharm

import ast

sum = eval("66+32")
print(sum)

print(ast.literal_eval("{'name':'linux'}"))

print(eval("{'name':num,'age':33}", {"num": 18}))

age = 10

print(eval("{'name':'linux','age':age}"),{"age":18}, locals())
