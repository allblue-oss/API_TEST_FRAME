#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/15 13:58
# @Author : 杜云慧
# @Site : 
# @File : config_utils.py
# @Software: PyCharm

import configparser


class ConfigUtils():
    def __init__(self, config_path):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path,encoding='utf-8')

    def read_value(self, section, key):
        value = self.cfg.get(section, key)
        return value
