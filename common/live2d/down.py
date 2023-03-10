import os

import requests
import var

request_url_path = "https://live2d.fghrsh.net/api/model/"
request_url = request_url_path + '{}/{}'

out_path = '/Users/xin/Frontend/blog/themes/keep/source/live2d_api/model/'


def file(dir):
    print('当前目录：' + dir)
    if not test(dir):
        os.makedirs(dir)


def test(dir):
    return os.path.isdir(dir)


def get_model(model):
    print('当前模型：' + model)
    model_out_path = os.path.join(out_path, model)
    file(model_out_path)
    index = requests.get(request_url.format(model, 'index.json'))
    index_json = index.json()
    with open(os.path.join(model_out_path, 'index.json'), 'wb') as f:
        f.write(index.content)  # 这句话自带文件关闭功能，不需要再写f.close()
    model_moc = requests.get(request_url.format(model, index_json['model'])).content
    with open(os.path.join(model_out_path, index_json['model']), 'wb') as f:
        f.write(model_moc)
    if 'physics' in index_json:
        physics = requests.get(request_url.format(model, index_json['physics'])).content
        with open(os.path.join(model_out_path, index_json['physics']), 'wb') as f:
            f.write(physics)
    for texture in index_json['textures']:
        texture_path = os.path.join(model_out_path, texture.split('/')[0])
        file(texture_path)
        with open(os.path.join(texture_path, texture.split('/')[1]), 'wb') as f:
            texture_content = requests.get(request_url.format(model, texture)).content
            f.write(texture_content)
    if 'pose' in index_json:
        file(os.path.join(model_out_path, os.path.dirname(index_json['pose'])))
        pose = requests.get(request_url.format(model, index_json['pose'])).content
        with open(os.path.join(model_out_path, index_json['pose']), 'wb') as f:
            f.write(pose)
    if 'expressions' in index_json:
        for expresstion in index_json['expressions']:
            expresstion_real_file_path = os.path.abspath(os.path.join(model_out_path, expresstion['file']))
            file(os.path.dirname(expresstion_real_file_path))
            expresstion_file_content = requests.get(
                os.path.join(request_url_path, os.path.relpath(expresstion_real_file_path, out_path))).content
            with open(expresstion_real_file_path, 'wb') as f:
                f.write(expresstion_file_content)
    if 'motions' in index_json:
        for motions in index_json['motions'].values():
            for mtn in motions:
                file_real_file_path = os.path.abspath(os.path.join(model_out_path, mtn['file']))
                file(os.path.dirname(file_real_file_path))
                mtn_file_content = requests.get(
                    os.path.join(request_url_path, os.path.relpath(file_real_file_path, out_path))).content
                with open(file_real_file_path, 'wb') as f:
                    f.write(mtn_file_content)
                if 'sound' in mtn:
                    sound_real_file_path = os.path.abspath(os.path.join(model_out_path, mtn['sound']))
                    file(os.path.dirname(sound_real_file_path))
                    sound_file_content = requests.get(
                        os.path.join(request_url_path, os.path.relpath(sound_real_file_path, out_path))).content
                    with open(sound_real_file_path, 'wb') as f:
                        f.write(sound_file_content)
    print('当前模型：{},输出成功'.format(model))


if __name__ == '__main__':
    for models in var.model_list['models']:
        if type(models) == list:
            for model in models:
                get_model(model)
        else:
            get_model(models)