#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/15 13:47
# @Author : 杜云慧
# @Site : 
# @File : config_demo.py
# @Software: PyCharm

import os
import configparser

config_path = os.path.join(os.path.dirname(__file__), '..', 'conf/config.ini')

cfg = configparser.ConfigParser()
cfg.read(config_path,encoding='utf-8')
print(cfg.get('path','CASE_DATA_PATH'))
