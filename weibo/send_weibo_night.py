import requests
from io import BytesIO
import json
import time

access_token = 'xx'

url = "https://api.weibo.com/2/statuses/share.json"


def get_msg():
    url = "http://api.tianapi.com/txapi/one/index"
    params = {"key": "xx"}
    text = requests.get(url=url, params=params).text
    msg = json.loads(text)
    print(msg.get('newslist')[0])
    return msg.get('newslist')[0]


def send(text, img_src):
    # POST请求，发表微博
    # 构建POST参数
    params = {
        "access_token": access_token,
        "status": text +" https://mynamecoder.com/about/"
    }
    # 构建二进制multipart/form-data编码的参数
    response = requests.get(img_src)
    image = BytesIO(response.content)
    files = {
        #     网络
        "pic": image
        #     本地
        # "pic" : open(img_src,"rb")
    }
    res = requests.post(url, data=params, files=files)
    print(res.text)

if __name__ == '__main__':
    # 格式化成2016-03-20 11:45:39形式
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    msg = get_msg()
    send("[月亮]"+msg.get('word')+"晚安。", msg.get('imgurl'))