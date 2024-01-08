import requests
import time
import json

'''
爬取专业列表
'''

request_url='https://lx-appapi-v2.eiceducation.com.cn/api/v2/Major?keyword=&countryName=&majorMageClass=&majorSubClass=&ClassType=&page={}&limit={}'
request_detail_url='https://lx-appapi-v2.eiceducation.com.cn/api/v2/Major/{}'

page=1
limit=100
result = requests.get(request_url.format(page,limit))
result_json = result.json()
total = result_json['count']
print('总记录数：',total)
limit=len(result_json['data'])
# 获取result_json['data']，类型为list的长度')
limit=len(result_json['data'])
# 获取result_json['data']，类型为list的长度
print('每页返回记录数：',limit)
major_list=[]
marjor_detail_list = []

def out(my_list,file_name):
    # 打开文件以写入
    with open(file_name, 'w', encoding='utf-8') as file:
        # 遍历列表
        for item in my_list:
            # 将每个元素写入文件，并在每个元素后添加换行符
            file.write(json.dumps(item,ensure_ascii=False) + '\n')

for i in range(total//limit):
    major_result = requests.get(request_url.format(i+1,limit))
    major_result_json = major_result.json()
    for marjor in major_result_json['data']:
        # print(marjor)
        major_list.append(marjor)
    print('page:',i+1)
    # time.sleep(1)
    # 将marjor放入list中，然后输出到文件
    for marjor in major_result_json['data']:
        current_request_detail_url = request_detail_url.format(marjor['CrmMajorId'])
        # print(current_request_detail_url,marjor['Id'])
        # time.sleep(1)
        marjor_detail_result = requests.get(current_request_detail_url)
        # print(result.json())
        json_obj = marjor_detail_result.json()
        # print(json.dumps(json_obj['data'],ensure_ascii=False))
        marjor_detail_list.append(json_obj['data'])
    #     break
    if i == 3:
        break

out(major_list,'major_list.json')
out(marjor_detail_list,'marjor_detail_list.json')
