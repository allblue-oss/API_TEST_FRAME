#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/23 14:46
# @Author : 杜云慧
# @Site : 
# @File : xlutils_demo01.py
# @Software: PyCharm

import os
import xlrd
from xlutils.copy import copy
from API_TEST_FEAME.common.localconfig_utils import local_config

excel_path = os.path.join(os.path.dirname(__file__), '..',local_config.CASE_DATA_PATH)
wb = xlrd.open_workbook(excel_path, formatting_info=True)  # 创建工作簿对象 xlrd模块2007 2003

new_workbook = copy(wb)  # new_workbook 已经变成可写的对象 xlwt对象
sheet = new_workbook.get_sheet(wb.sheet_names().index('Sheet1'))
sheet.write(1,14,'pass')
sheet.write(2,14,'fail')
new_workbook.save(excel_path)
