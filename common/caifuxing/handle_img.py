import re
import os
import uuid

import requests
import cai_fu_xing


def traverse_dir_files(root_dir, ext=None, is_sorted=True):
    """
    列出文件夹中的文件, 深度遍历
    :param root_dir: 根目录
    :param ext: 后缀名
    :param is_sorted: 是否排序，耗时较长
    :return: [文件路径列表, 文件名称列表]
    """
    names_list = []
    paths_list = []
    for parent, _, fileNames in os.walk(root_dir):
        for name in fileNames:
            if name.startswith('.'):  # 去除隐藏文件
                continue
            if ext:  # 根据后缀名搜索
                if name.endswith(tuple(ext)):
                    names_list.append(name)
                    paths_list.append(os.path.join(parent, name))
            else:
                names_list.append(name)
                paths_list.append(os.path.join(parent, name))
    if not names_list:  # 文件夹为空
        return paths_list, names_list
    return paths_list, names_list


# 保存函数
def save_image(img_link, file_path):
    img_byte = requests.get(url=img_link).content
    with open(file_path, 'wb') as f:
        f.write(img_byte)


if __name__ == '__main__':
    root_dir = "/Users/xin/Documents/study/caifuxing/"
    for parent, dirs, fileNames in os.walk(root_dir):
        for name in fileNames:
            if name.startswith('.') or not name.endswith("html"):  # 去除隐藏文件
                continue
            file_path = os.path.join(parent, name)
            print(file_path)
            cai_fu_xing.request_cft().file(os.path.join(parent, 'img'))
            from htmlwebshot import WebShot
            shot = WebShot()
            shot.quality = 100
            image = shot.create_pic(html="file.html")
            continue
            with open(file_path,) as html:
                content = html.read()
                matches = re.findall(r'\ssrc="([^"]+)"', content)
                for i, old_img_url in enumerate(matches):
                    print("图片链接:" + old_img_url)
                    if not old_img_url.startswith('http'):
                        continue
                    new_img_name = uuid.uuid4().__str__() + os.path.splitext(old_img_url)[-1]
                    img_path = os.path.join(parent, 'img', new_img_name)
                    new_img_relative_path = os.path.join('img', new_img_name)
                    # new_img_relative_path = './img/' + str(i) + ".png"

                    save_image(old_img_url, img_path)
                    content = content.replace(old_img_url, new_img_relative_path)
                # 输出html
                with open(file_path, "w") as f:
                    f.write(content)  # 这句话自带文件关闭功能，不需要再写f.close()
