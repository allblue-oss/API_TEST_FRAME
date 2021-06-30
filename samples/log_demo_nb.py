#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/30 9:47
# @Author : 杜云慧
# @Site : 
# @File : log_demo_nb.py
# @Software: PyCharm

import os
from nb_log import LogManager

# l_path = os.path.join (os.path.dirname(__file__),'pythonlogs')
# print(l_path)

logger = LogManager('dyh').get_logger_and_add_handlers(log_filename='ApiTest.log')
print('你好')
logger.info('hello')
logger.warning('警告')
logger.error('这是错误日志')








































