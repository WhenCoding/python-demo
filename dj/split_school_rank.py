import json

# 读取 JSON 文件
with open('/Users/xin/Desktop/school_rank.json', 'r') as file:
    data = json.load(file)

# 将数据分为两个部分
part1 = data[:len(data)//2]
part2 = data[len(data)//2:]

# 将两个部分分别保存为 JSON 文件
with open('./school_rank_part1.json', 'w') as file:
    json.dump(part1, file, ensure_ascii=False)

with open('./school_rank_part2.json', 'w') as file:
    json.dump(part2, file, ensure_ascii=False)
