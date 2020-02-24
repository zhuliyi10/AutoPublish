from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import ui
import sys
from videobean import VideoBean

#这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog,QHBoxLayout,QVBoxLayout,QLineEdit
from qwindow import Qwindow


def uploadTaoTiao(videoBean):
    wait = ui.WebDriverWait(browser, 10)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    # # 今日头条上传视频
    browser.get("https://mp.toutiao.com/profile_v3/xigua/upload-video?index=0")
    sleep(3)
    # browser.find_element_by_css_selector(".byte-btn").click()
    browser.find_element_by_xpath("//div[@class='byte-upload xigua-upload-video-trigger upload-video-trigger-card']/input").send_keys(
        videoBean.videoPath)
    # 等待页面加载
    wait.until(lambda driver: browser.find_element_by_xpath(
        "//span[@class='percent']"))

    
    browser.find_element_by_xpath("//textarea[@class='byte-textarea abstract']").send_keys(
        videoBean.desc)
    browser.find_element_by_xpath("//div[@class='xigua-input-wrapper']/input").send_keys(
        videoBean.title)
    print("开始上传")
    status = browser.find_element_by_xpath("//span[@class='percent']").text
    while status != "上传成功":
        print(status)
        sleep(5)
        status = browser.find_element_by_xpath("//span[@class='percent']").text
    print("上传成功")

def onPublishVideo(videoBean):
        print(videoBean.title)
        print(videoBean.desc)
        print(videoBean.videoPath)
        print(videoBean.picPath)
        uploadTaoTiao(videoBean)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    ex=Qwindow(onPublishVideo)
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    browser = webdriver.Chrome("D:\install\python\python37\Scripts\chromedriver.exe", chrome_options=chrome_options)
    browser.maximize_window()
    sys.exit(app.exec_())






