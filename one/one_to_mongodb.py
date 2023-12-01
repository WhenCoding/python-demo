#!/usr/bin/python3

import pymongo
import requests
import threading
import time


def one():
    """
    获取一条一言。
    :return:
    """
    url = "https://v1.hitokoto.cn/"
    return requests.get(url).json()


# 原先的 print 函数和主线程的锁
_print = print
mutex = threading.Lock()


# 定义新的 print 函数
def print(text, *args, **kw):
    """
    使输出有序进行，不出现多线程同一时间输出导致错乱的问题。
    """
    with mutex:
        _print(text, *args, **kw)


if __name__ == "__main__":
    myclient = pymongo.MongoClient(
        "mongodb://xx.mongodb.rds.aliyuncs.com:3717",
        authSource="admin")
    mydb = myclient['one']
    mycol = mydb["sentence"]
    list = []
    i = 0
    while i < 100:
        res = one()
        print(res["hitokoto"] + " ----" + res["from"])
        list.append(res)
        time.sleep(1)
        i += 1
    x = mycol.insert_many(list)
    print(x.inserted_ids)
