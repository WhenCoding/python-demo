from selenium import webdriver
import time
import requests

from selenium.common.exceptions import NoSuchElementException

account_list = [{"username": "mynamecoder@163.com", "password": "lovetoday#29"},
                {"username": "17092163015", "password": "coder#1024"}]
options = webdriver.ChromeOptions()
# todo linux 需要设置 有界面或者无界面
# options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')



def sign(browser):
    # try:
       browser.find_element_by_id("homeheader-signin").click()
    # except Exception as e:
        # sign(browser)
        # print(e)


def login_by_email():
    current_date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print("开始签到：" + current_date_time)
    error_account_infos = []
    for account in account_list:
        try:
            browser = webdriver.Chrome(options=options)
            browser.get("https://devcloud.huaweicloud.com/bonususer/home/costbonus")
            time.sleep(2)
            name = browser.find_element_by_xpath("//*[@id='personalAccountInputId']/input")
            name.send_keys(account['username'])
            passwd = browser.find_element_by_xpath("//*[@id='personalPasswordInputId']/input")
            passwd.send_keys(account['password'])
            login_button = browser.find_element_by_id("btn_submit")
            time.sleep(2)
            login_button.click()
            time.sleep(5)
            sign(browser)
        except Exception as e:
            print(account['username'] + "签到失败")
            error_msg = "原因：可能是未找到元素"
            print(error_msg)
            print(e)
            error_account_infos.append({"account": account['username'], "reason": error_msg})
        else:
            print(account['username']+"签到成功！")
        finally:
            browser.close()
    msg = current_date_time + "\n"
    if error_account_infos:
        msg = msg + "那个...辛先生，您有签到失败的账号...😢"
    else:
        msg = msg + "辛先生！今天，所有账户均签到成功！🌹"
    send_text(msg)


def send_text(msg):
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=e88a795a-6215-4e4f-807c-111f356655f2"
    headers = {"Content-Type": "text/plain"}
    data = {
        "msgtype": "text",
        "text": {
            "content": msg,
            "mentioned_mobile_list": ["13137437121"]
        }
    }
    r = requests.post(url, headers=headers, json=data)
    print("消息发送结果：" + r.text)


if __name__ == '__main__':
    login_by_email()
