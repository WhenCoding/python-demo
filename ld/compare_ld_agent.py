import json




# 读取两个json文件
with open('ld_agent_old.json', 'r', encoding='utf-8') as file:
    ld_agent_old_json = json.load(file)

with open('ld_agent.json', 'r', encoding='utf-8') as file:
    ld_agent = json.load(file)

# 提取所有的 labels 到一个数组中
ld_agent_old = []
for item in ld_agent_old_json:
    ld_agent_old.extend(item["labels"])


matched_pairs = []
unmatched_ld_agent_old = []
unmatched_ld_agent = []

# 寻找对应关系
for user_old in ld_agent_old:
    matched = False
    for user in ld_agent:
        if user_old["id"] == user["id"]:
            matched_pairs.append((user_old, user))
            matched = True
            break
    if not matched:
        unmatched_ld_agent_old.append(user_old)

# 找到在ld_agent中，但不在ld_agent_old中的对象
for user in ld_agent:
    found = False
    for pair in matched_pairs:
        if user == pair[1]:
            found = True
            break
    if not found:
        unmatched_ld_agent.append(user)

print("对应关系：")
for pair in matched_pairs:
    print(f"老系统： {pair[0]}")
    print(f"新系统： {pair[1]}\n")

print("\n新系统中没有的：")
for user_old in unmatched_ld_agent_old:
    print(f"{user_old}")

print("\n老系统中没有的：")
for user in unmatched_ld_agent:
    print(f"{user}")