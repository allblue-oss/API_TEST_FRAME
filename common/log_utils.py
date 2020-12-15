#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/15 15:48
# @Author : 杜云慧
# @Site : 
# @File : log_utils.py
# @Software: PyCharm

import os
import logging
import time
from common.localconfig_utils import local_config

current_path = os.path.dirname(__file__)
log_out_path = os.path.join(current_path, '..', local_config.LOG_PATH)


class LogUtils():
    def __init__(self, log_path=log_out_path):
        self.log_name = os.path.join(log_out_path, 'ApiTest_%s.log' % time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger(("ApiTestlog"))
        self.logger.setLevel(local_config.LOG_LEVEL)

        console_handler = logging.StreamHandler()  # 控制台输出
        file_handler = logging.FileHandler(self.log_name, 'a', encoding='utf-8')  # 文件输出
        formatter = logging.Formatter("[%(asctime)s]' %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %("
                                      "message)s")
        # '[%(asctime)s]' %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s] : %(message)s'
        # %(asctime)s %(name)s %(levelname)s %(message)s
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)  # 防止打印日志重复
        self.logger.addHandler(file_handler)  # 防止打印日志重复

        console_handler.close()
        file_handler.close()

    def get_logger(self):
        return self.logger


logger = LogUtils().get_logger()    # 防止打印日志重复

if __name__ == '__main__':
    logger.info('hello')
