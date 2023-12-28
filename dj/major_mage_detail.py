import requests
import time
import json

'''
爬取专业列表-详情
'''

# 原始请求：https://lx-appapi-v2.eiceducation.com.cn/api/v2/SchoolRank?type=2&keyword=&countryNames=%E8%8B%B1%E5%9B%BD%2C%E7%BE%8E%E5%9B%BD&minRank=&maxRank=&page=1&limit=10
request_url='https://lx-appapi-v2.eiceducation.com.cn/api/v2/SchoolRank?page={}&limit={}'
request_url_detail='https://lx-appapi-v2.eiceducation.com.cn/api/v2/Major?keyword=&countryName=&majorMageClass=&majorSubClass=&ClassType=&page={}&limit={}'

school_list=[]
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
school_detail_dict = {}


for i in range(total//limit):
    result = requests.get(request_url.format(i+1,limit))
    result_json = result.json()
    # for school in result_json['data']:
    #     print(school)
    print('page:',i+1)
    time.sleep(1)
    # 将school放入list中，然后输出到文件
    for school in result_json['data']:
        if school['SchoolId'] in school_detail_dict or school['SchoolId'] is None:
            continue
        current_request_detail_url = request_detail_url.format(school['SchoolId'])
        # print(current_request_detail_url,school['Id'])
        time.sleep(2)
        result = requests.get(current_request_detail_url)
        # print(result.json())
        json_obj = json.loads(result.json())
        # print(json.dumps(json_obj['rows'],ensure_ascii=False))
        if 'rows' in json_obj:
            school_detail_dict[school['SchoolId']] = json.dumps(json_obj['rows'],ensure_ascii=False)    
    # break
# 遍历字典的值
for value in school_detail_dict.values():
    print(value)
