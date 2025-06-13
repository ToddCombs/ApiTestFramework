# -*- coding:utf-8 -*-
# @Author   :ToddCombs
# @Time     :2025/6/13 10:31
# @File     :api_client.py
# @Software :PyCharm
# 接口&压力测试客户端

import requests
import json
import time

# from gevent.pywsgi import headers_factory

from config.config import BASE_URL, HEADERS
from src.utils import setup_logger
from locust import FastHttpUser,task, between

class APIClient:
    '''
    通用API客户端，封装requests的调用，方便接口测试使用。
    '''
    def __init__(self,BASE_URL):
        self.BASE_URL = BASE_URL

    def get(self, endpoint, params=None,headers=None):
        '''
        发起GET请求
        :param endpoint:
        :param params:
        :param headers:
        :return:
        '''
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.get(url, params=params, headers=headers)
        return response

    def post(self, endpoint, data=None, json=None, headers=None):
        '''
        发起POST请求
        :param endpoint:
        :param data:
        :param json:
        :param headers:
        :return:
        '''
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.post(url, data=data, json=json, headers=headers)
        return response

    def put(self, endpoint, data=None, json=None,headers=None):
        '''
        发起PUT请求
        :param endpoint:
        :param data:
        :param json:
        :param headers:
        :return:
        '''
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.put(url, data=data, json=json, headers=headers)
        return response

    def delete(self, endpoint, headers=None):
        '''
        发起DELETE请求
        :param endpoint:
        :param headers:
        :return:
        '''
        url = f"{self.BASE_URL}{endpoint}"
        response = requests.delete(url, headers=headers)
        return response

# ==================================Locust压力测试部分=======================
class LocustUser(FastHttpUser):
    """
    Locust压力测试用户类，用来模拟用户行为，基于HttpUserLocust使用的是异步请求方式，
    与requests的同步方式不同。
    """
    wait_time = between(1, 3)   # 模拟用户操作间隔时间。

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 初始化一些变量，比如token
        self.token = None

    def on_start(self):
        '''
        模拟用户登录，获取token
        :return:
        '''
        login_data = {
            "username": "testuser",
            "password": "testpass"
        }
        with self.client.post("/login", json=login_data, catch_response=True) as response:
            if response.status_code == 200:
                self.token = response.json().get("token")
            else:
                response.failure("登录失败")

    @task
    def get_user_info(self):
        """
        模拟获取用户信息的接口调用
        :return:
        """
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else{}
        self.client.get("/user/info", headers=headers)

    @task
    def create_post(self):
        """
        模拟创建帖子的接口调用
        :return:
        """
        headers = {"Authorization": f"Bearer {self.token}"} if self.token else{}
        post_data = {
            "title": "Locust No.1!",
            "content": "test post "
        }
        self.client.post("/posts", json=post_data, headers=headers)