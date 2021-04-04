import requests
from io import BytesIO
import json
import time
# 刘文朋
# access_token = '2.00r9ympF0WoQcZd71aa0044dHGYLGB'
access_token = '2.00g6pZNE0WoQcZd81de3716buPgpUC'

url = "https://api.weibo.com/2/statuses/share.json"


def get_msg():
    url = "http://api.tianapi.com/txapi/saylove/index"
    params = {"key": "6c6f404af4e09207be9c10f632a768a3"}
    text = requests.get(url=url, params=params).text
    msg = json.loads(text)
    print(msg.get('newslist')[0])
    return msg.get('newslist')[0]


def send(text):
    # POST请求，发表微博
    # 构建POST参数
    params = {
        "access_token": access_token,
        "status": text +" https://mynamecoder.com/about/"
    }

    res = requests.post(url, data=params)
    print(res.text)

if __name__ == '__main__':
    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    msg = get_msg()
    send("[小红花]"+msg.get('content')+" 午安～")