import json
import os
import requests

base_path = os.path.dirname(os.path.abspath(__file__))
save_folder = base_path + "/major_detail"  # 指定的本地文件夹路径
school_list = []
oss_path = 'major_detail/img/'

def download_image(url, folder_path):
    # 创建文件夹
    os.makedirs(folder_path, exist_ok=True)

    # 发送请求并保存图片
    try:
        response = requests.get(url)
        if response.status_code == 200:
            file_name = url.split("/")[-1]
            file_path = os.path.join(folder_path, url.split("/")[-1])
            with open(file_path, "wb") as file:
                file.write(response.content)
            print("图片下载成功！")
            return file_name
        else:
            print("图片下载失败！")
    except Exception as e:
        # 处理其他所有异常，并将异常对象e保存在变量中
        print("发生了异常：", url)
    return ''


with open(base_path + '/major_detail.json', 'r') as f:
    for line in f:
        json_obj = json.loads(line)
        # 对json对象进行处理
        print(json_obj['LxSchoolLogo'])
        file_path = download_image(json_obj['LxSchoolLogo'],save_folder)
        json_obj['LxSchoolLogo']=oss_path + file_path
        school_list.append(json_obj)
        # break
        

# 打开文件，准备写入数据
with open(base_path + "/major_detail_turn_img.json", "w") as f:
    # 遍历数组中的每个JSON对象
    for obj in school_list:
        # 将JSON对象转换为字符串
        json_str = json.dumps(obj, ensure_ascii=False)
        # 将json字符串写入文件中，每个对象一行
        f.write(json_str)
        f.write("\n")
        