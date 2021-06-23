#!/usr/bin/env python
# encoding: utf-8
# @author: liusir
# @file: unittest_demo02.py
# @time: 2020/7/19 11:09 上午

import unittest
import paramunittest

# 元组类型可以
# @paramunittest.parametrized(
#     (8,5),
#     (10,20)
# )
#列表类型可以
# @paramunittest.parametrized(
#     [8,5],
#     [10,20]
# )
# 字典类型数据
# @paramunittest.parametrized(
#     {'numa':8,'numb':5},
#     {'numa':10,'numb':520}
# )

#函数或者数据对象传入进去
testdata = [{'numa':8,'numb':5},{'numa':10,'numb':520},{'numa':100,'numb':66}]
def get_data():
    return [{'numa':8,'numb':5},{'numa':1000,'numb':520},{'numa':100,'numb':66}]

@paramunittest.parametrized(
    *get_data()
)

class UTestDemo(paramunittest.ParametrizedTestCase):
    def setParameters(self, numa,numb):
        self.numa = numa
        self.numb = numb

    def test_number(self):
        print( 'numa=%d,mumb=%d'%(self.numa,self.numb) )
        self.assertGreater(self.numa,self.numb)

if __name__=="__main__":
    unittest.main()


