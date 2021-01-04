#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/4 14:37
# @Author : 杜云慧
# @Site : 
# @File : jsonpath_demo.py
# @Software: PyCharm

import jsonpath

d1 = {"access_token":"40_nYjftwBtPr7wqpIhpTpoEXiNieLDz5wbI-oEm52o2eL3s1k_o8E9jwtNUXN6sLYQCyD3qM2W93smdaA80TwKOYBu0MOT2ON-2pr4TtpbDIX3CrmlergtMH_jVW52irEXBsESfX2sFrPc8bp7QBEaAGAJUX","expires_in":7200}

print(d1["access_token"])


print(jsonpath.jsonpath(d1,'$.access_token')[0])

















