#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/14 17:06
# @Author : 杜云慧
# @Site : 
# @File : testdata_utils.py
# @Software: PyCharm
'''处理表格数据'''

import os
# from common.excel_utils import ExcelUtils
# from common import config
# from common.localconfig_utils import local_config

from API_TEST_FEAME.common.excel_utils import ExcelUtils
from API_TEST_FEAME.common.localconfig_utils import local_config

current_path = os.path.dirname(__file__)
test_data_path = os.path.join(current_path, '..', local_config.CASE_DATA_PATH)


class TestdataUtils():
    def __init__(self, test_data_path=test_data_path):
        self.test_data_path = test_data_path
        self.test_data = ExcelUtils(test_data_path, 'Sheet1').get_sheet_data_by_dict()

    def __get_testcase_data_dict(self):
        '''通过字典方式获取数据'''
        testcase_dict = {}
        for row_data in self.test_data:
            testcase_dict.setdefault(row_data['测试用例编号'], []).append(row_data)
        return testcase_dict

    def def_testcase_data_list(self):
        testcase_list = []
        for k, v in self.__get_testcase_data_dict().items():
            one_case_dict = {}
            one_case_dict["case_name"] = k
            one_case_dict["case_info"] = v
            testcase_list.append(one_case_dict)
        return testcase_list


if __name__ == "__main__":
    testdataUtils = TestdataUtils()
    for i in testdataUtils.def_testcase_data_list():
        print(i)
