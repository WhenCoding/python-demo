import os
import requests
import cai_fu_xing
import screenshot


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
    root_dir = "/Users/xin/Documents/study/caifuxing-img/"
    for parent, dirs, fileNames in os.walk(root_dir):
        for name in fileNames:
            if name.startswith('.') or not name.endswith("html"):  # 去除隐藏文件
                continue
            file_path = os.path.join(parent, name)
            print(file_path)
            img_name = os.path.splitext(name)[0]
            screenshot.screen("file://" + file_path, os.path.join(parent, img_name + '.png'))
