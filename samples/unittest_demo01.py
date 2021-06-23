#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/6/18 11:39
# @Author : 杜云慧
# @Site : 
# @File : unittest_demo01.py
# @Software: PyCharm

import unittest


class TestDemo(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_add(self):
        self.assertEqual(1 + 2, 3)


if __name__ == '__main__':
    unittest.main()
