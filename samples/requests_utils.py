#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/17 12:01
# @Author : 杜云慧
# @Site : 
# @File : requests_utils.py
# @Software: PyCharm

import ast
import requests
import jsonpath
from common.localconfig_utils import local_config


class RequestsUtils():
    def __init__(self):
        self.hosts = local_config.URL
        self.headers = {"ContentType": "application/json;charset=utf-8"}
        self.session = requests.session()
        self.temp_variables = {}  # 存放临时变量

    def __get(self, get_info):
        url = self.hosts + get_info["请求地址"]
        response = self.session.get(url=url,
                                    params=ast.literal_eval(get_info["请求参数(get)"])
                                    )
        response.encoding = response.apparent_encoding
        if get_info['取值方式'] == "json取值":
            value = jsonpath.jsonpath(response.json(),get_info['取值代码'])[0]
            print("jsonpath取值:"+value)
            print('**************')
            self.temp_variables[ get_info["传值变量"] ] = value
            print(self.temp_variables)
        result = {
            'code': 0,  # 请求是否成功的标志位
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_header': response.headers,
            'response_body': response.text  # 返回网页/json
        }
        return result

    def __post(self, post_info):
        url = self.hosts + post_infos["请求地址"]
        print(url)
        response = self.session.post(url=url,
                                     headers=self.headers,
                                     params=ast.literal_eval(post_info["请求参数(get)"]),
                                     # data = post_infos(post)["提交数据([post)"],
                                     json=ast.literal_eval(post_info["提交数据（post）"])
                                     )
        response.encoding = response.apparent_encoding
        if post_info['取值方式'] == "json取值":
            value = jsonpath.jsonpath(response.json(),post_info['取值代码'])[0]
            print("jsonpath取值:"+value)
            print('**************')
            self.temp_variables[ post_info["传值变量"] ] = value
            print(self.temp_variables)
        result = {
            'code': 0,  # 请求是否成功的标志位
            'response_reason': response.reason,
            'response_code': response.status_code,
            'response_header': response.headers,
            'response_body': response.text  # 返回网页/json
        }

        return result

    def request(self,step_info):

        '''发送请求，判断请求方式'''

        request_type = step_info["请求方式"]
        if request_type == "get":
            result = self.__get(step_info)
        elif request_type == "post":
            result = self.__post(step_info)
        else:
            result = {'code':1,'result':'请求方式不支持'}
        print("服务器返回结果:"+result['response_body'])
        return result

    def request_by_step(self,step_infos):
        for step_info in step_infos:
            temp_result = self.request(step_info)
            if temp_result['code']!=0:
                break
        return temp_result



if __name__ == "__main__":
    get_infos = {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'}
    # get_infos = {'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01',
    #              '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token',
    #              '请求参数(get)': '{"grant_type":"client_credential","appid":"wxdd1e072d49643bf0","secret":"c6868a07c562c932292eabdccda250a6"}',
    #              '提交数据（post）': '', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键是否存在',
    #              '期望结果': 'access_token,expires_in'}

    RequestsUtils().request(get_infos)
    ##  字符串转为字典  eval()函数

    post_infos = {'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02', '接口名称': '删除标签接口',
                  '请求方式': 'post', '请求地址': '/cgi-bin/tags/delete', '请求参数(get)': '{"access_token":${token}}',
                  '提交数据（post）': '{"tag":{"id":409}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': 'json键值对',
                  '期望结果': '{"errcode":0,"errmsg":"ok"}'}
    # RequestsUtils().request(get_infos)
    # RequestsUtils().request(post_infos)

    # case_info = [{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01', '接口名称': '获取access_token接口', '请求方式': 'get', '请求地址': '/cgi-bin/token', '请求参数(get)': '{"grant_type":"client_credential","appid":"wx55614004f367f8ca","secret":"65515b46dd758dfdb09420bb7db2c67f"}', '提交数据（post）': '', '取值方式': 'json取值', '传值变量': 'token', '取值代码': '$.access_token', '期望结果类型': '正则匹配', '期望结果': '{"access_token":"(.+?)","expires_in":(.+?)}'}, {'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02', '接口名称': '创建标签接口', '请求方式': 'post', '请求地址': '/cgi-bin/tags/create', '请求参数(get)': '{"access_token":${token}}', '提交数据（post）': '{"tag" : {"name" : "衡东8888"}}', '取值方式': '无', '传值变量': '', '取值代码': '', '期望结果类型': '正则匹配', '期望结果': '{"tag":{"id":(.+?),"name":"衡东8888"}}'}]
    #
    # requestsUtils = RequestsUtils()
    #
    # for c in case_info:
    #     requestsUtils.request(c)