# -*- coding:utf-8 -*-
# @Author   :ToddCombs
# @Time     :2025/6/13 10:30
# @File     :config.py
# @Software :PyCharm
# 全局配置文件，主要存储(URL, Headers等)
BASE_URL = "https://baidu.com"
HEADERS = {
    "Content-type": "application/json",
    "Authorization": "Bearer mytoken"
}

TIMEOUT = 10    # 请求超时时间秒