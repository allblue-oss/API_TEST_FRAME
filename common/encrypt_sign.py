#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/17 15:19
# @Author : 杜云慧
# @Site : 
# @File : encrypt_sign.py
# @Software: PyCharm

import json
import requests
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA1
import base64
from common.localconfig_utils import local_config

def rsa_sign(message):
    msg = message.encode('utf-8')
    private_key = RSA.importKey(
        ('-----BEGIN RSA PRIVATE KEY-----\n' + local_config.PRIVATE_KEY + '\n-----END RSA PRIVATE KEY-----').encode(
            'utf-8'))
    # private_key = RSA.importKey(key)
    ## message做“哈希”处理，RSA签名这么要求的
    hash_obj = SHA1.new(msg)
    signature = PKCS1_v1_5.new(private_key).sign(hash_obj)
    return base64.b64encode(signature)


biz_content = json.dumps({"merchant_id": "900029000000354"})  # 要进行加密的数据
sign = rsa_sign(biz_content)
data = {"sign": sign, "charset": "UTF-8", "biz_content": biz_content,
        "partner": "900029000000354", "sign_type": "RSA", "service": "trade.acc.balance"}
res = requests.post("https://test_nucc.bhecard.com:9088/api_gateway.do", data)
print(res.text)
