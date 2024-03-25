import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

session = requests.Session()
retry = Retry(total=5, backoff_factor=0.1)
adapter = HTTPAdapter(max_retries=retry)
session.mount('https://', adapter)

'''
爬取销售动态
'''

request_url = "https://lxcrm.weiwenjia.com/api/pc/customers/{}/sales_activities"
headers = {

}



def get_sales_activities(customer_id):
    page = 1

    params = {
        "page": page,
    }

    result = session.get(request_url.format(customer_id), headers=headers, params=params)
    limit=200
    result_json = result.json()['data']
    total = result_json['total_count']
    total_pages = result_json['total_pages']
    print('返回条数:%d'%(len(result_json['list'])))
    sales_activities_list = []
    for i in range(total_pages):
        params['page'] = i + 1
        sales_activities_result = session.get(request_url.format(customer_id), headers=headers, params=params)
        sales_activities_result_json = sales_activities_result.json()
        for sales_activities in sales_activities_result_json['data']['list']:
            # print(sales_activities)
            sales_activities_list.append(sales_activities)
        print('客户：%s 销售动态-第%s页已获取' %(customer_id,params['page']))
    return sales_activities_list

if __name__ == "__main__":
    get_sales_activities('541460428')