import json

# 读取json文件
with open('/Users/xin/Desktop/school_rank.json', 'r') as f:
    data = json.load(f)

# 将对象逐行写入文件
with open('school_rank_format.json', 'w') as f:
    for item in data:
        json.dump(item, f,  ensure_ascii=False)
        f.write('\n')
