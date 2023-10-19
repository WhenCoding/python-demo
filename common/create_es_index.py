from elasticsearch import Elasticsearch
import json
import datetime
import requests
qyapi_url="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=77b1b9c6-6fdf-4a98-9568-8ae551701e99"
indices_list=["printmedia","twitter","web","wechat","search","blog","app","shortvideo","tvvideo","forum","tieba","netvideo","facebook","weibo"]
today=datetime.date.today()
es=Elasticsearch(["192.168.17.30:9210"])
tomorrow =  (today + datetime.timedelta(days=1)).strftime('%Y%m%d')  # 用今天日期加上时间差，参数为1天，获得明天的日期
for indice in indices_list:
  results="True"
  aa="yqms_"+str(tomorrow)+"_"+indice
  get_indices_results=(es.indices.exists(aa))
  get_indices_results=(str(get_indices_results))
  if get_indices_results == results:
    get_indices_results=(str(get_indices_results))
  else:
    send_msg = {
            "msgtype": "text",
            "text": {
                "content": "创建索引"+aa+"失败",
            },
        }
    qywx_headers = {
        'Content-Type': 'application/json',
    }
    ret = requests.post(qyapi_url, data=json.dumps(send_msg), headers=qywx_headers)
    print(ret.text)