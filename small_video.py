from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import ui
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys
from videobean import VideoBean

#这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog,QHBoxLayout,QVBoxLayout,QLineEdit
from qwindow import Qwindow


# 上传今日头条小视频
def uploadTaoTiao(videoBean):
    wait = ui.WebDriverWait(browser, 100)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    # # 今日头条上传视频
    browser.get("https://mp.toutiao.com/profile_v3/smallvideo/publish")
    sleep(3)
    # browser.find_element_by_css_selector(".byte-btn").click()
    browser.find_element_by_xpath("//div[@class='sv-publish-top']/input").send_keys(
        videoBean.videoPath)
    # 等待页面加载
    print("开始上传今日头条小视频")
    wait.until(lambda driver: browser.find_element_by_xpath("//div[@class='sv-video-uploaded']"))

    # 上传封面
    browser.find_element_by_xpath("//span[@class='sv-video-change-cover']").click()
    sleep(2)
    browser.find_element_by_xpath("//div[@class=' upload-handler']/input").send_keys(videoBean.picPath)
    sleep(2)
    browser.find_element_by_xpath("//button[@class='tui2-btn tui2-btn-size-default tui2-btn-primary pgc-button']").click()
    sleep(5)
    browser.find_element_by_xpath("//textarea[@class='tui2-input']").send_keys(videoBean.title)
    browser.find_element_by_xpath("//button[@class='tui2-btn tui2-btn-size-small tui2-btn-primary publish-btn']").click()    
    print("今日头条小视频上传成功")
#上传全民小视频
def uploadQuanming(videoBean):
    wait = ui.WebDriverWait(browser, 100)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://mcn.baidu.com/publish/upload")
    sleep(3)
    browser.find_element_by_xpath("//span[@class='ant-upload ant-upload-btn']/input").send_keys(videoBean.videoPath)
    # 等待页面加载
    print("开始上传全民小视频")
    wait.until(lambda driver: browser.find_element_by_xpath("//div[@class='success___1dnqC']"))
    print("全民小视频上传成功")
    browser.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()  
    sleep(0.3)
    browser.find_element_by_xpath("//div[@class='video-vertical-cover___3QmJj']/img").click()
    sleep(3)
    browser.find_element_by_xpath("//span[@class='ant-upload ant-upload-btn']/input").send_keys(videoBean.picPath)
    sleep(2)
    browser.find_element_by_xpath("//textarea[@class='ant-input']").send_keys(videoBean.title)
    browser.find_element_by_xpath("//button[@class='ant-btn btn-publish___3FDWl ant-btn-primary']").click()  

# 上传快手小视频
def uploadKuaishou(videoBean):
    wait = ui.WebDriverWait(browser, 100)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://cp.kuaishou.com/article/publish/video")
    sleep(3)
    browser.find_element_by_xpath("//div[@class='el-upload el-upload--text']/input").send_keys(
        videoBean.videoPath)
    # 等待页面加载
    print("开始上传快手小视频")
    wait.until(lambda driver: browser.find_element_by_xpath("//i[@class='iconfont icon-check-succeed green']"))
    browser.find_element_by_xpath("//div[@class='edit-container']//input").send_keys(videoBean.picPath)
    sleep(2)
    browser.find_element_by_xpath("//textarea[@class='el-textarea__inner']").send_keys(videoBean.title)
    browser.find_element_by_xpath("//div[@class='container__content__body']//button[@class='el-button el-button--primary el-button--medium']").click()
    print("快手小视频上传成功")


# 上传抖音小视频
def uploadDouyin(videoBean):
    wait = ui.WebDriverWait(browser, 100)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://media.douyin.com/#/upload")
    sleep(3)
    browser.find_element_by_xpath("//label[@class='upload-btn--9eZLd']/input").send_keys(
        videoBean.videoPath)
    # 等待页面加载
    print("开始上传抖音小视频")

    wait.until(lambda driver: browser.find_element_by_xpath("//div[@class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr']"))
    print("抖音小视频上传成功")
    browser.find_element_by_xpath("//div[@class='notranslate public-DraftEditor-content']").click()
    ActionChains(browser).send_keys(videoBean.title).perform()
    browser.find_element_by_xpath("//button[@class='button--1SZwR primary--1AMXd fixed--3rEwh']").click()   


# 上传大鱼号小视频
def uploadDayu(videoBean):
    wait = ui.WebDriverWait(browser, 100)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://mp.dayu.com/dashboard/minivideo/write?spm=a2s0i.db_article_write.content.3.7e293caatzoXXJ")
    sleep(3)
    browser.find_element_by_xpath("//input[@class='webuploader-element-invisible']").send_keys(videoBean.videoPath)
    # 等待页面加载
    print("开始上传大鱼号小视频")
    browser.find_element_by_xpath("//input[@id='SCOPE_titletext']").send_keys(videoBean.title)
    sleep(2)
    browser.find_element_by_xpath("//div[@class='w-form-field-content']/input[@type='file']").send_keys(videoBean.picPath)
    sleep(8)
    browser.find_element_by_xpath("//button[text()='保存']").click()   
    sleep(3)
    status = browser.find_element_by_xpath("//p[@class='converting_video_name']").text
    while status == "":
        sleep(2)
        status = browser.find_element_by_xpath("//p[@class='converting_video_name']").text
    print("大鱼号小视频上传成功")
    # cover=browser.find_element_by_xpath("//div[@class='minivideo-cover']")
    # ActionChains(browser).move_to_element(cover).perform()
    # browser.find_element_by_xpath("//div[@class='minivideo-cover']//button[text()='从视频截图中选择']").click()   
    # wait.until(lambda driver: browser.find_element_by_xpath("//div[@class='article-material-image_image-choose']//div"))
    # browser.find_element_by_xpath("//div[@class='article-material-image_image-choose']//div").click()   
    # browser.find_element_by_xpath("//button[text()='下一步']").click()   
    # sleep(2)
    # browser.find_element_by_xpath("//button[text()='保存']").click()   
    # sleep(8)
    
    browser.find_element_by_xpath("//div[@class='minivideo_opt']//button[@class='w-btn w-btn_primary']").click()   


# 上传爱奇艺小视频
def uploadIqiyi(videoBean):
    wait = ui.WebDriverWait(browser, 100)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://mp.iqiyi.com/wemedia/publish/videoLte")
    sleep(6)
    browser.find_element_by_xpath("//input").send_keys(videoBean.videoPath)
    sleep(8)
    browser.find_element_by_xpath("//input[@class='mp-upload__input']").send_keys(videoBean.picPath)
    sleep(5)
    wait.until(lambda driver: browser.find_element_by_xpath("//i[@class='mp-iconsvg svg-complete rt']"))
    sleep(2)
    browser.find_element_by_xpath("//input[@class='mp-input__inner']").send_keys(Keys.CONTROL + "a")
    browser.find_element_by_xpath("//input[@class='mp-input__inner']").send_keys(videoBean.title)
    browser.find_element_by_xpath("//button[@class='mp-button mp-button--success is-animate']").click() 
def onPublishVideo(videoBean):
        print(videoBean.title)
        print(videoBean.desc)
        print(videoBean.videoPath)
        print(videoBean.picPath)
        uploadTaoTiao(videoBean)
        uploadQuanming(videoBean)
        uploadKuaishou(videoBean)
        uploadDouyin(videoBean)
        uploadDayu(videoBean)
        uploadIqiyi(videoBean)


if __name__ == "__main__":
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    # browser = webdriver.Chrome("D:\install\python\python37\Scripts\chromedriver.exe", chrome_options=chrome_options)
    browser = webdriver.Chrome("D:\intsall\Anaconda3\Scripts\chromedriver.exe", chrome_options=chrome_options)
    # browser.maximize_window()
    # sleep(3)
    app=QApplication(sys.argv)
    ex=Qwindow(onPublishVideo)
    sys.exit(app.exec_())
    
    






