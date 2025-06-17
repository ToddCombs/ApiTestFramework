# -*- coding:utf-8 -*-
# @Author   :ToddCombs
# @Time     :2025/6/13 10:30
# @File     :config.py
# @Software :PyCharm
# 全局配置文件，主要存储(URL, Headers等)
BASE_URL = "http://v.juhe.cn"
API_KEY = "e78ca8aa9ff7462762aaed05f50b37d3"
INDEX_ENDPOINT = f"{BASE_URL}/toutiao/index"
CONTENT_ENDPOINT = f"{BASE_URL}/toutiao/content"

HEADERS = {
    "Content-type": "application/x-www-form-urlencoded"
}

NEWS_CATEGORIES = {
    "top": "推荐",
    "guonei": "国内",
    "guoji": "国际",
    "yule": "娱乐",
    "tiyu": "体育",
    "junshi": "军事",
    "keji": "科技",
    "caijing": "财经",
    "youxi": "游戏",
    "qiche": "汽车",
    "jiankang": "健康"
}
TIMEOUT = 10    # 请求超时时间秒
