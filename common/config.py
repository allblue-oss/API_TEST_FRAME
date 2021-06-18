#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/15 14:03
# @Author : 杜云慧
# @Site : 
# @File : config.py
# @Software: PyCharm

import os
# from common.config_utils import ConfigUtils
from API_TEST_FEAME.common.config_utils import ConfigUtils

config_path = os.path.join(os.path.dirname(__file__), '..', 'conf/config.ini')
configUtils = ConfigUtils(config_path)

URL = configUtils.read_value('default','URL')
CASE_DATA_PATH = configUtils.read_value('path','CASE_DATA_PATH')

