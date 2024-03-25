import json




# 读取两个json文件
with open('E:\Projects\python-demo\ld\sys_user_old.json', 'r', encoding='utf-8') as file:
    sys_user_old = json.load(file)

with open('E:\Projects\python-demo\ld\sys_user.json', 'r', encoding='utf-8') as file:
    sys_user = json.load(file)






# sys_user_old = [
#     {"id": 1, "name": "Alice"},
#     {"id": 2, "name": "Bob"},
#     {"id": 3, "name": "Charlie"}
# ]

# sys_user = [
#     {"user_id": 1, "age": 25},
#     {"user_id": 2, "age": 30},
#     {"user_id": 4, "age": 28}
# ]

matched_pairs = []
unmatched_sys_user_old = []
unmatched_sys_user = []

# 寻找对应关系
for user_old in sys_user_old:
    matched = False
    for user in sys_user:
        if user_old["id"] == user["user_id"]:
            matched_pairs.append((user_old, user))
            matched = True
            break
    if not matched:
        unmatched_sys_user_old.append(user_old)

# 找到在sys_user中，但不在sys_user_old中的对象
for user in sys_user:
    found = False
    for pair in matched_pairs:
        if user == pair[1]:
            found = True
            break
    if not found:
        unmatched_sys_user.append(user)

print("对应关系：")
for pair in matched_pairs:
    print(f"老系统： {pair[0]}")
    print(f"新系统： {pair[1]}\n")

print("\n新系统中没有的：")
for user_old in unmatched_sys_user_old:
    print(f"{user_old}")

print("\n老系统中没有的：")
for user in unmatched_sys_user:
    print(f"{user}")

