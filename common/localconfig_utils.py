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

    @property  # 把方法变为属性方法
    def URL(self):
        url_value = self.cfg.get('default', 'URL')
        return url_value

    @property
    def CASE_DATA_PATH(self):
        case_data_path_value = self.cfg.get('path', 'CASE_DATA_PATH')
        return case_data_path_value

    @property
    def LOG_PATH(self):
        log_path_value = self.cfg.get('path', 'LOG_PATH')
        return log_path_value

    @property
    def LOG_LEVEL(self):
        log_level_value = int(self.cfg.get('log', 'LOG_LEVEL'))
        return log_level_value

    @property
    def PRIVATE_KEY(self):
        private_key_value = self.cfg.get('easypay_test_merchant_info', 'PRIVATE_KEY')
        return private_key_value

    @property
    def REPORT_PATH(self):
        report_path_value = self.cfg.get('path', 'REPORT_PATH')
        return report_path_value

    @property
    def CASE_PATH(self):
        case_path_value = self.cfg.get('path', 'CASE_PATH')
        return case_path_value

    @property
    def SMTP_SERVER(self):
        smtp_server_value = self.cfg.get('email', 'smtp_server')
        return smtp_server_value

    @property
    def SMTP_PASSWORD(self):
        smtp_password_value = self.cfg.get('email', 'smtp_password')
        return smtp_password_value

    @property
    def SMTP_SENDER(self):
        smtp_sender_value = self.cfg.get('email', 'smtp_sender')
        return smtp_sender_value

    @property
    def SMTP_RECEIVER(self):
        smtp_receiver_value = self.cfg.get('email', 'smtp_receiver')
        return smtp_receiver_value

    @property
    def SMTP_CC(self):
        smtp_cc_value = self.cfg.get('email', 'smtp_cc')
        return smtp_cc_value

    @property
    def SMTP_SUBJECT(self):
        smtp_subject_value = self.cfg.get('email', 'smtp_subject')
        return smtp_subject_value

    '''若配置文件有新增，应在此处新增属性方法'''


local_config = LocalconfigUtils()  # 创建对象

if __name__ == '__main__':
    config = LocalconfigUtils()
    print(local_config.CASE_PATH)
