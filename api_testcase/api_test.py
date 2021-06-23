#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/18 15:15
# @Author : 杜云慧
# @Site : 
# @File : api_test.py
# @Software: PyCharm

import warnings
import unittest
import paramunittest
from API_TEST_FEAME.common.testdata_utils import TestdataUtils
from API_TEST_FEAME.common.requests_utils import RequestsUtils

case_infos = TestdataUtils().def_testcase_data_list()


@paramunittest.parametrized(
    *case_infos
)
class APITest(paramunittest.ParametrizedTestCase):
    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)

    def setParameters(self, case_id, case_info):
        self.case_id = case_id
        self.case_info = case_info

    def test_api_common_function(self):
        '''测试描述'''
        self._testMethodName = self.case_info[0].get('测试用例编号')
        self._testMethodDoc = self.case_info[0].get('测试用例名称')
        actual_result = RequestsUtils().request_by_step(self.case_info)
        print(actual_result)
        self.assertTrue(actual_result.get('check_result'),actual_result.get('message'))


if __name__ == '__main__':
    unittest.main()
