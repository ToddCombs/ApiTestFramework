# -*- coding:utf-8 -*-
# @Author   :ToddCombs
# @Time     :2025/6/17 10:05
# @File     :api_test.py
# @Software :PyCharm
# 接口测试脚本

import requests
from config.config import API_KEY, INDEX_ENDPOINT, CONTENT_ENDPOINT, NEWS_CATEGORIES
from icecream import ic

def test_toutiao_index(category="top"):
    """
    测试新闻头条列表接口
    :return:
    """
    params = {
        "key": API_KEY,
        "type": category,
        "page": 1,
        "page_size": 10,
        "is_filter": 1
    }
    response = requests.get(INDEX_ENDPOINT, params=params)

    if response.status_code == 200:
        data = response.json()
        if data["resultcode"] == "200":
            ic(f"【接口测试】toutiao/index({NEWS_CATEGORIES.get(category, category)})成功！")
            for news in data["result"]["data"]:
                ic(f"标题:{news['title']}")
        else:
            ic(f"【接口测试】toutiao/index({NEWS_CATEGORIES.get(category, category)})错误:{data['reason']}")
    else:
        ic(f"【接口测试】toutiao/index({NEWS_CATEGORIES.get(category, category)})请求失败，HTTP状态码：{response.status_code}")

def test_toutiao_content():
    """
    测试头条详情接口
    :return:
    """
    params = {
        "uniquekey": "82e20b98cd61122f0a38e6ec87edc7cb",   # 输入有效的新闻ID
        "key": API_KEY
    }
    response = requests.get(CONTENT_ENDPOINT,params=params)

    if response.status_code == 200:
        data = response.json()
        if data["resultcode"] == "200":
            ic("【接口测试】toutiao/content 成功！")
            ic(f"标题：{data['result']['title']}")
        else:
            ic(f" 【接口测试】toutiao/content 错误：{data['reason']}")
    else:
        ic(f" 【接口测试】toutiao/content 请求失败，HTTP状态码：{response.status_code}")

if __name__ == '__main__':
    # 测试所有分类的头条接口
    for category in NEWS_CATEGORIES.keys():
        test_toutiao_index(category)

    test_toutiao_content()