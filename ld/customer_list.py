import time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

session = requests.Session()
retry = Retry(total=5, backoff_factor=0.1)
adapter = HTTPAdapter(max_retries=retry)
session.mount('https://', adapter)

import json

from operation_logs import get_operation_logs
from sales_activities import get_sales_activities


'''
爬取客户列表
'''

request_url = "https://lxcrm.weiwenjia.com/api/pc/v1/customers/pc_index"

headers = {

}

page = 1
per_page=200


data = {
    "current": page,
    "pageSize": per_page,
    "total": 0,
    "followModel": False,
    "sort":"created_at",
    "order":"asc",
    # "filters": [
    #     {
    #         "name": "status",
    #         "query": "29471017",
    #         "operator": "equal"
    #     }
    # ],
    "advanced_filters": [],
    "page": page,
    "per_page": per_page
}

# 记录程序开始时间
start_time = time.time()


result = session.post(request_url, headers=headers, json=data)
result_json = result.json()['data']
total = result_json['total_count']
total_pages = result_json['total_pages']
print('总记录数：%d , 总页数：%d , 每页返回记录数：%d' %(total,total_pages,per_page))
customer_list=[]
customer_detail_list = []

def out(my_list,file_name):
    # 打开文件以写入
    with open(file_name, 'w', encoding='utf-8') as file:
        # 遍历列表
        for item in my_list:
            # 将每个元素写入文件，并在每个元素后添加换行符
            file.write(json.dumps(item,ensure_ascii=False) + '\n')

try:
    for i in range(total_pages):
        data['current'] = i + 1
        data['page'] = i + 1
        customer_result = session.post(request_url, headers=headers, json=data)
        customer_result_json = customer_result.json()
        for customer in customer_result_json['data']['list']:
            # print(customer)
            customer['operation_logs'] = get_operation_logs(customer['id'])
            customer['sales_activities'] = get_sales_activities(customer['id'])
            customer_list.append(customer)
            # break
        print('客户列表-第%s页已获取' %page)
        time.sleep(1)

        if len(customer_list) == 2000:
            out(customer_list,'customer_list_'+ str(i) + '.json')
            customer_list.clear()
        
        # if i == 2:
        #     break

except requests.exceptions.RequestException as e:
    # 处理连接异常
    print("连接异常:", e)


# 计算程序执行时间
end_time = time.time()
execution_time = end_time - start_time

print(f"程序执行时长：{execution_time} 秒")

out(customer_list,'customer_list_final.json')

