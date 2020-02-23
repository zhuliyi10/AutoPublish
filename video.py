from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import ui

def isuploadSuccess():
    print("开始上传")
    status=browser.find_element_by_xpath("//span[@class='percent']").text
    while status!="上传成功":
        print(status)
        sleep(5)
        status=browser.find_element_by_xpath("//span[@class='percent']").text
    print("上传成功")
chrome_options=Options()
chrome_options.add_experimental_option("debuggerAddress","127.0.0.1:9222")
browser=webdriver.Chrome("D:\install\python\python37\Scripts\chromedriver.exe",chrome_options=chrome_options)
wait = ui.WebDriverWait(browser,10)#10秒内每隔500毫秒扫描1次页面变化
# 今日头条上传视频
browser.get("https://mp.toutiao.com/profile_v3/xigua/upload-video?index=0")
browser.maximize_window()
sleep(3)
# browser.find_element_by_css_selector(".byte-btn").click()
browser.find_element_by_xpath("//div[@class='byte-upload xigua-upload-video-trigger upload-video-trigger-card']/input").send_keys("F:\\羽毛球\\羽联赛事\\20马来西亚大师赛\\十佳球\\混双\\雅思组合\\1.mp4")
#等待页面加载
wait.until(lambda driver: browser.find_element_by_xpath("//span[@class='percent']"))
isuploadSuccess()


