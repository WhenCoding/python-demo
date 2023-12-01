import requests
import base64
from io import BytesIO
import hashlib
import os


def urltobase64(url):
    # 图片保存在内存
    response = requests.get(url)
    # 得到图片的base64编码
    return base64.b64encode(BytesIO(response.content).read())

def get_md5_of_file(img_path):
    response = requests.get(img_path)
    myhash = hashlib.md5()
    myhash.update(BytesIO(response.content).read())
    return myhash.hexdigest()

def send_img():
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xx"
    headers = {"Content-Type": "text/plain"}
    img_path = "https://img.mynamecoder.com/anney_hansewei.gif"
    imgbase64 = str(urltobase64(img_path), 'utf-8')
    imgmd5 = get_md5_of_file(img_path)
    print(imgbase64)
    print(imgmd5)
    data = {
          "msgtype": "image",
        "image": {
            "base64": imgbase64,
            "md5": "0e797ff1a76bcb6af80da8c91b9d933a"
        }
       }
    r = requests.post(url, headers=headers, json=data)
    print(r.text)


def send_text(msg):
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xx"
    headers = {"Content-Type": "text/plain"}
    data = {
            "msgtype": "text",
            "text": {
                "content": msg,
                "mentioned_mobile_list": ["13137437121"]
            }
       }
    r = requests.post(url, headers=headers, json=data)
    print(r.text)


if __name__ == '__main__':
    send_text()

