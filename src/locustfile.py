# -*- coding:utf-8 -*-
# @Author   :ToddCombs
# @Time     :2025/6/13 10:31
# @File     :locustfile.py
# @Software :PyCharm
#locustfile.py
fromlocustimportHttpUser,task,between
fromconfigimportAPI_KEY,INDEX_ENDPOINT,CONTENT_ENDPOINT,NEWS_CATEGORIES
importrandom

classNewsApiUser(HttpUser):
wait_time=between(1,3)#模拟用户请求间隔（1~3秒）

@task
deftest_toutiao_index(self):
"""模拟用户访问头条分类接口（随机选择分类）"""
#随机选择一个分类
category=random.choice(list(NEWS_CATEGORIES.keys()))
params={
"type":category,
"key":API_KEY
}
withself.client.get(INDEX_ENDPOINT,params=params,catch_response=True)asresponse:
ifresponse.status_code==200:
data=response.json()
ifdata["resultcode"]!="200":
response.failure(f"API返回错误:{data['reason']}")
else:
response.failure(f"HTTP状态码异常:{response.status_code}")

@task(3)#权重设为3，表示更频繁地调用此接口
deftest_toutiao_content(self):
"""模拟用户访问头条详情接口"""
params={
"id":"123456",#替换成有效的新闻ID
"key":API_KEY
}
withself.client.get(CONTENT_ENDPOINT,params=params,catch_response=True)asresponse:
ifresponse.status_code==200:
data=response.json()
ifdata["resultcode"]!="200":
response.failure(f"API返回错误:{data['reason']}")
else:
response.failure(f"HTTP状态码异常:{response.status_code}")


