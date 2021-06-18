#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/17 13:43
# @Author : 杜云慧
# @Site : 
# @File : importdata_demo.py
# @Software: PyCharm

# 使用excel中的数据去驱动requests_utils

from API_TEST_FEAME.common.testdata_utils import TestdataUtils
from API_TEST_FEAME.common.requests_utils import RequestsUtils

all_case_info = TestdataUtils().def_testcase_data_list()
case_info = all_case_info[2].get('case_info')
# print(RequestsUtils().request_by_step(case_info))
# RequestsUtils().request_by_step(case_info)

for case_info in all_case_info:
    RequestsUtils().request_by_step(case_info.get('case_info'))