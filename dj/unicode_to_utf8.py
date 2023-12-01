import json
import codecs

# 读取 JSON 文件
with open('/Users/xin/Desktop/school_rank.json', 'r') as f:
    data = json.load(f)

# 序列化为 UTF-8 编码的 JSON 字符串
json_str = json.dumps(data, ensure_ascii=False).encode('utf-8')

# 输出到文件
with codecs.open('/Users/xin/Desktop/school_rank_utf8.json', 'w', encoding='utf-8') as f:
    f.write(json_str.decode('utf-8'))
