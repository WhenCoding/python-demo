import requests
import time
import json

'''
爬取高校排名
'''

# 原始请求：https://lx-appapi-v2.eiceducation.com.cn/api/v2/SchoolRank?type=2&keyword=&countryNames=%E8%8B%B1%E5%9B%BD%2C%E7%BE%8E%E5%9B%BD&minRank=&maxRank=&page=1&limit=10
request_url='https://lx-appapi-v2.eiceducation.com.cn/api/v2/SchoolRank?page={}&limit={}'

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

for i in range(total//limit):
    result = requests.get(request_url.format(i+1,limit))
    result_json = result.json()
    for school in result_json['data']:
        print(school)
    print('page:',i+1)
    time.sleep(1)
    # 将school放入list中，然后输出到文件
    school_list.append(school)

with open('school_rank.json', 'w') as f:
    json.dump(school_list, f,ensure_ascii=False).encode('utf-8')
    f.close()
    print('school_rank.json saved')



# with open(os.path.join(model_out_path, 'index.json'), 'wb') as f:
#     f.write(index.content)  # 这句话自带文件关闭功能，不需要再写f.close()