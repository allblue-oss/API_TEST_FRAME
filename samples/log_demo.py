#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/15 15:32
# @Author : 杜云慧
# @Site : 
# @File : log_demo.py
# @Software: PyCharm

import logging

logger = logging.getLogger("logger")
logger.setLevel(10)  #10,20,30,40,50
handler1 = logging.StreamHandler()    #输出到控制台
handler1.setLevel(30)
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
handler1.setFormatter(formatter)
logger.addHandler(handler1)


handler2 = logging.FileHandler('./test.log','a',encoding='utf-8')
handler2.setLevel(10)
handler2.setFormatter(formatter)
logger.addHandler(handler2)

logger.info("hello")
