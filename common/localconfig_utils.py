#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/15 14:11
# @Author : 杜云慧
# @Site : 
# @File : localconfig_utils.py
# @Software: PyCharm

import os
import configparser

current_path = os.path.dirname(__file__)
config_path = os.path.join(current_path, '..', 'conf/config.ini')


class LocalconfigUtils():
    def __init__(self, config_path=config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path, encoding='utf-8')

    @property      #把方法变为属性方法
    def URL(self):
        url_value = self.cfg.get('default', 'URL')
        return url_value

    @property
    def CASE_DATA_PATH(self):
        case_data_path_value = self.cfg.get('path', 'CASE_DATA_PATH')
        return case_data_path_value

    '''若配置文件有新增，应在此处新增属性方法'''


local_config = LocalconfigUtils()  #创建对象


if __name__ == '__main__':
    config = LocalconfigUtils()
    print(local_config.CASE_DATA_PATH)