import asyncio
import time

from pyppeteer import launch

html_url = 'http://wechat.ewrwefg.com/pushwarningdetail?uuid=a336131c290711edb1bfe4434ba66c88&infoid=a336131c290711edb1bfe4434ba66c88&openid=735ostdt1AWVKQfVENFN9hsomc1Fll083-5&appkey=yqms'
img_path = '/Users/xin/Desktop/test.png'


async def start_screenshot(html_url, img_path):
    # launch chromium browser in the background
    browser = await launch()
    # open a new tab in the browser
    page = await browser.newPage()
    # add URL to a new page and then open it
    await page.goto(html_url)
    # time.sleep(5)
    # create a screenshot of the page and save it
    await page.screenshot({"path": img_path, "fullPage": True})
    # close the browser
    await browser.close()


def screen(html_url, img_path):
    print("Starting...")
    asyncio.get_event_loop().run_until_complete(start_screenshot(html_url, img_path))
    print("Screenshot has been taken")


if __name__ == '__main__':
    screen(html_url,img_path)
