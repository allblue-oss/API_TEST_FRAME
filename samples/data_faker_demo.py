#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/28 17:08
# @Author : 杜云慧
# @Site : 
# @File : data_faker_demo.py
# @Software: PyCharm

from faker import Faker

f =Faker(locale='zh_CN')

for i in range(10):
    print(f.name()+':'+f.ssn())