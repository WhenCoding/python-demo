import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

session = requests.Session()
retry = Retry(total=5, backoff_factor=0.1)
adapter = HTTPAdapter(max_retries=retry)
session.mount('https://', adapter)

'''
爬取操作日志
'''

request_url = "https://lxcrm.weiwenjia.com/api/pc/operation_logs"
headers = {

}



def get_operation_logs(customer_id):
    page = 1
    per_page = 10

    params = {
        "loggable_type": "customer",
        "loggable_id": customer_id,
        "page": page,
        "per_page": per_page,
        "category": ""
    }

    result = session.get(request_url, headers=headers, params=params)
    result_json = result.json()['data']
    total = result_json['total_count']
    total_pages = result_json['total_pages']
    print('返回条数:%d'%(len(result_json['list'])))
    operation_logs_list = []
    for i in range(total_pages):
        params['page'] = i + 1
        operation_logs_result = session.get(request_url, headers=headers, params=params)
        operation_logs_result_json = operation_logs_result.json()
        for operation_logs in operation_logs_result_json['data']['list']:
            # print(operation_logs)
            operation_logs_list.append(operation_logs)
        print('客户：%s 操作日志-第%s页已获取' %(customer_id,params['page']))
        if i == 1:
            break
    return operation_logs_list

if __name__ == "__main__":
    get_operation_logs('541183378')