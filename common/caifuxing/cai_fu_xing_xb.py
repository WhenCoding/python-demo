import json
import os
import time

from urllib3 import encode_multipart_formdata
import turn_to_audio
import turn_m3u8
import requests

# 小白
list_url = "https://zapi.caifuxingketang.com/xb/grant/caifu/xiaobai/list/"
detail_url = "https://zapi.caifuxingketang.com/xb/caifu/course/chapter/detail/"
voice_detail_url = "https://zapi.caifuxingketang.com/xb/grant/caifu/course/voice/detail/"
# todo 更换文件夹
path = "/Users/xin/Documents/study/caifuxing/小白理财训练营/"


class request_cft():
    header = {}
    list_param = {}

    def file(self, dir):
        if not self.test(dir):
            os.makedirs(dir)

    def test(self, dir):
        return os.path.isdir(dir)

    def prepare_header(self):
        request_cft.header = {
            "Host": "zapi.caifuxingketang.com",
            "t": "TNyg2Q6PPVtqLoezXPp7mcZQJ+zLJURNB3NP5KJ+ZEfIpaLnSpQU0wxrMc0809Ive2CXSy4HjA69PWsft/J90URZ2WFUUHdwe8qlfIHa6s8dMb/cFPT7iB/IKAyC/EIbyC3+iRW7yMgf+LQXVwIm9+Dr5Wso4wqg3grttp7jpLYxektA9gE3lLNnHgVh6J9JdgOM0TRasORCcGLtbFV5z8rSL2n7o8+ppGj6HpfxhYSc50fXgZP5X2fmuamNAr9rwuWzsgMqjNRiqIJjYNQo25wE9mquj13nDtKPyPYDbCCrrcTTk3Z/ua9lIEDvqo7ddfC+tIgGg7GV2gQ24fvRIV7giiznt6+uKlBrDQvZb1ffXY4i9oav22oGzWU9fXWIWqbei/6Wj+b8bpaJ/0AW4+DNcWcRBdRqFgndlV/UJBwwD6piBW67WyYgEWfv8wQdzyJydoY7/o5f9fmSzMujWw==",
            "Accept": "*/*",
            "User-Agent": "WealthClasses/1.13 (iPhone; iOS 15.5; Scale/3.00)",
            "Accept-Language": "zh-Hans-CN;q=1, zh-Hant-CN;q=0.9",
            "Referer": "https://api.shayujizhang.com/",
        }
    # todo 需要更改 course_id sign tms 即可切换下一个课程
    def get_list(self):
        request_cft.list_param = {
            "course_id": "1",
            "sign": "9213eb",
            "tms": "1660617758.949722",
            "appName": "Course",
            "appVersion": "1.13",
            "channel": "AppStore",
            "client": "iPhone",
            "deviceType": "iPhone12,5",
            "deviceVersion": "15.5",
            "guest_id": "",
            "idfa": "",
            "lan": "zh-Hans-CN",
            "lat": "0",
            "lon": "0",
            "network": "WiFi",
            "number_id": "15706345",
            "uid": "2A3VpoTT3mVc4SHAUK9enH",
            "uuid": "05D969FE-E91C-4316-AE68-88ED0CE166FA",
        }
        # 转换data数据的类型
        encode_data = encode_multipart_formdata(request_cft.list_param)
        request_cft.list_param = encode_data[0]
        request_cft.header['Content-Type'] = encode_data[1]
        res = requests.post(url=list_url, headers=request_cft.header, data=request_cft.list_param)
        return json.loads(res.content.decode('utf-8'))

    def get_detail(self, cha_id):
        detail_param = {"appName": "Course", "appVersion": "1.13", "channel": "AppStore",
                        "client": "iPhone", "course_id": "5", "deviceType": "iPhone12,5", "deviceVersion": "15.5",
                        "guest_id": "", "idfa": "", "lan": "zh-Hans-CN", "lat": "0", "lon": "0", "network": "WiFi",
                        "number_id": "15706345", "query_evaluate": "3", "sign": "c8ce6b", "tms": "1660487849.881519",
                        "uid": "2A3VpoTT3mVc4SHAUK9enH", "uuid": "05D969FE-E91C-4316-AE68-88ED0CE166FA",
                        'cha_id': cha_id}
        # 转换data数据的类型
        encode_data = encode_multipart_formdata(detail_param)
        request_cft.detail_param = encode_data[0]
        request_cft.header['Content-Type'] = encode_data[1]
        res = requests.post(url=detail_url, headers=request_cft.header, data=request_cft.detail_param)
        return json.loads(res.content.decode('utf-8'))

    def get_voice_detail(self, cha_id):
        detail_param = {"appName": "Course",
                        "appVersion": "1.13",
                        "cha_id": cha_id,
                        "channel": "AppStore",
                        "client": "iPhone",
                        "deviceType": "iPhone12,5",
                        "deviceVersion": "15.5",
                        "guest_id": "",
                        "idfa": "",
                        "lan": "zh-Hans-CN",
                        "lat": "0",
                        "lon": "0",
                        "network": "WiFi",
                        "number_id": "15706345",
                        "sign": "b06b29",
                        "tms": "1660574164.350885",
                        "uid": "2A3VpoTT3mVc4SHAUK9enH",
                        "uuid": "05D969FE-E91C-4316-AE68-88ED0CE166FA",
                        "voice_type": "1", }
        # 转换data数据的类型
        encode_data = encode_multipart_formdata(detail_param)
        request_cft.detail_param = encode_data[0]
        request_cft.header['Content-Type'] = encode_data[1]
        res = requests.post(url=voice_detail_url, headers=request_cft.header, data=request_cft.detail_param)
        return json.loads(res.content.decode('utf-8'))


if __name__ == '__main__':
    cft = request_cft()
    cft.prepare_header()
    list_info = cft.get_list()
    chapter_infos = list_info["data"]["chapter_info"]
    for chapter_info in chapter_infos:
        dir = str(chapter_info["chapter_name"])
        out_path = path + dir + "/"
        print("输出至目录:" + out_path)
        cft.file(out_path)
        for chapter in chapter_info["chapter_list"]:
            time.sleep(3)
            cha_id = chapter["cha_id"]
            name = chapter["name"]
            detail_info = cft.get_detail(cha_id)
            content_html = detail_info["data"]["content"]
            # 输出html
            with open(out_path + name + ".html", "w") as f:
                f.write(content_html)  # 这句话自带文件关闭功能，不需要再写f.close()
            # 输出音频
            voice_detail = cft.get_voice_detail(cha_id)
            turn_m3u8.m3u8_url = voice_detail["data"]["voice_url"]
            turn_m3u8.video_download_path = out_path
            turn_m3u8.save_mp4_path = out_path
            turn_m3u8.save_temporary_ts_path = out_path + 'temporary_ts'
            cft.file(turn_m3u8.save_temporary_ts_path)
            turn_m3u8.save_mp4_name = name + ".mp4"
            mp4_file_path = out_path + turn_m3u8.save_mp4_name
            turn_m3u8.begin()
            my_clip = turn_to_audio.extract_audio(mp4_file_path)
            mp3_file_path = out_path + name + ".mp3"
            my_clip.write_audiofile(mp3_file_path)
            # 删除mp4
            if os.path.exists(mp4_file_path):
                # removing the file using the os.remove() method
                os.remove(mp4_file_path)
                break
