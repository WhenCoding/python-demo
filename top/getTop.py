import requests
from bs4 import BeautifulSoup as bs
import json

if __name__ == '__main__':

    url = 'https://tophub.today/'

    r = requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    })
    content = r.text
    soup = bs(content, 'html.parser')

    for f in soup.find(id="node-2").find_all(class_="cc-cd-cb-ll"):
        s = f.find(class_="s").text
        t = f.find(class_="t").text
        e = f.find(class_="e").text
        data = {"no": s,"content": t, "count": e}
        print(json.dumps(data, ensure_ascii=False))
