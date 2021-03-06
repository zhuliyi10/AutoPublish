from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
import sys
from videobean import VideoBean

#这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog,QHBoxLayout,QVBoxLayout,QLineEdit
from qwindow import Qwindow


# 今日头条
def uploadTaoTiao(videoBean):
    wait = ui.WebDriverWait(browser, 600)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://mp.toutiao.com/profile_v3/xigua/upload-video?index=0")
    sleep(3)
    browser.find_element_by_xpath("//div[@class='byte-upload xigua-upload-video-trigger upload-video-trigger-card']/input").send_keys(
        videoBean.videoPath)
    # 等待页面加载
    wait.until(lambda driver: browser.find_element_by_xpath("//span[@class='percent']"))

 
    print("开始上传今日头条")
    status = browser.find_element_by_xpath("//span[@class='percent']").text
    while status != "上传成功":
        print(status)
        sleep(5)
        status = browser.find_element_by_xpath("//span[@class='percent']").text
    print("今日头条上传成功")
    # sleep(2)
    # browser.find_element_by_xpath("//textarea[@class='byte-textarea abstract']").send_keys(
    #     videoBean.desc)
    # browser.find_element_by_xpath("//div[@class='xigua-input-wrapper']/input").send_keys(
    #     videoBean.title)
    browser.find_element_by_xpath("//div[@class='xigua-image-modify']//input").send_keys(videoBean.picPath)
    wait.until(lambda driver: browser.find_element_by_xpath("//button[@class='btn-l btn-sure ml14']"))
    browser.find_element_by_xpath("//button[@class='btn-l btn-sure ml14']").click()

    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(1)
    wait.until(lambda driver: browser.find_element_by_xpath("//div[@class='byte-select video-tags-select byte-select-size-large byte-select-multiple']"))
    sleep(1)
    browser.find_element_by_xpath("//div[@class='byte-select video-tags-select byte-select-size-large byte-select-multiple']").click()
    ActionChains(browser).send_keys("体育").send_keys(Keys.ENTER).perform()
    ActionChains(browser).send_keys("羽毛球").send_keys(Keys.ENTER).perform()
    ActionChains(browser).send_keys("赛事").send_keys(Keys.ENTER).perform()
    release=browser.find_element_by_xpath("//button[@class='byte-btn byte-btn-primary byte-btn-size-large byte-btn-shape-square action-footer-btn submit']").click()
    ActionChains(browser).click(release).perform()
    print("今日头条发表成功")


# 百家号
def uploadBaiJiaHao(videoBean):
    wait = ui.WebDriverWait(browser, 600)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://baijiahao.baidu.com/builder/rc/edit?type=video")
    sleep(3)
    print("开始百家号")
    browser.find_element_by_xpath("//div[@class='updataCoverBox']/input").send_keys(videoBean.videoPath)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(1)
    browser.find_element_by_xpath("//div[@class='container']").click()
    sleep(1)
    browser.find_element_by_xpath("//span[@class='ant-upload']/input").send_keys(videoBean.picPath)
    status=browser.find_element_by_xpath("//div[@class='status']/div[@class='progress']").text
    while status != "1张上传成功":
        print(status)
        sleep(2)
        status=browser.find_element_by_xpath("//div[@class='status']/div[@class='progress']").text
    sleep(3)
    browser.find_element_by_xpath("//button[@class='ant-btn ant-btn-primary']").click()
    tag=browser.find_element_by_xpath("//div[@class='client_components_tagInput']//input")
    tag.send_keys("体育")
    tag.send_keys(Keys.ENTER)
    tag.send_keys("羽毛球")
    tag.send_keys(Keys.ENTER)
    tag.send_keys("赛事")
    tag.send_keys(Keys.ENTER)

    # 等待页面加载
    wait.until(lambda driver: browser.find_element_by_xpath("//span[@class='okIcon']"))
    sleep(2)
    browser.find_element_by_xpath("//button[@class='ant-btn bjh-btn-normal op-publish ant-btn-primary']").click()
    print("百家号发表成功")



# 企鹅号
def uploadQiE(videoBean):
    wait = ui.WebDriverWait(browser, 600)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://om.qq.com/article/videoPublish")
    sleep(3)
    print("开始企鹅号")
    browser.find_element_by_xpath("//input").send_keys(videoBean.videoPath)
    browser.find_element_by_xpath("//button[@class='btn btn-default action-cover']").click()
    sleep(2)
    browser.find_element_by_xpath("//span[text()='图片上传']").click()
    sleep(1)
    browser.find_element_by_xpath("//input[@class='webuploader-element-invisible']").send_keys(videoBean.picPath)
    sleep(2)
    browser.find_element_by_xpath("//div[@class='pop-action']/button[@class='btn btn-primary']").click()
    sleep(5)
    tag=browser.find_element_by_xpath("//div[@class='tagsinput']//input")
    tag.send_keys("体育")
    tag.send_keys(Keys.ENTER)
    tag.send_keys("羽毛球")
    tag.send_keys(Keys.ENTER)
    tag.send_keys("赛事")
    tag.send_keys(Keys.ENTER)
    browser.find_element_by_xpath("//div[@class='chosen-container chosen-container-single']").click()
    browser.find_element_by_xpath("//div[@class='chosen-search']/input").send_keys("综合体育")
    sleep(1)
    browser.find_element_by_xpath("//li/em[text()='综合体育']").click()
    status=browser.find_element_by_xpath("//span[@class='text-title']").text
    while status != "共1个视频，已上传1个":
        sleep(5)
        status=browser.find_element_by_xpath("//span[@class='text-title']").text
    sleep(5)
    browser.find_element_by_xpath("//button[text()='发布']").click()
    print("企鹅号发表成功")


# 大鱼号
def uploadDaYu(videoBean):
    wait = ui.WebDriverWait(browser, 600)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://mp.dayu.com/dashboard/video/write?spm=a2s0i.db_article_write.content.2.63383caapef4p9")
    sleep(3)
    print("开始大鱼号")
    browser.find_element_by_xpath("//input").send_keys(videoBean.videoPath)
    sleep(3)
    browser.find_element_by_xpath("//div[@class='widgets-selects direction-horizontal']").click()
    sleep(1)
    browser.find_element_by_xpath("//a[text()='体育']").click()
    sleep(1)
    
    browser.find_element_by_xpath("//div[@id='coverImg']/input").send_keys(videoBean.picPath)
    sleep(8)
    browser.find_element_by_xpath("//div[@class='article-material-image-dialog_root']//button").click()
    sleep(3)
    
    browser.find_element_by_xpath("//div[@class='article-write_video-tags form-control']").click()
    sleep(1)
    ActionChains(browser).send_keys("体育").perform()
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    sleep(1)
    ActionChains(browser).send_keys("羽毛球").perform()
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    sleep(1)
    ActionChains(browser).send_keys("赛事").perform()
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    # 等待页面加载
    wait.until(lambda driver: browser.find_element_by_xpath("//div[@class='article-write_video-container-result-succeed']"))
    browser.find_element_by_xpath("//div[@class='container']//button[text()='发表']").click()
    sleep(3)
    browser.find_element_by_xpath("//button[text()='确认发表']").click()

# B站
def uploadBilibili(videoBean):
    wait = ui.WebDriverWait(browser, 600)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://member.bilibili.com/v2?spm_id_from=333.851.b_696e7465726e6174696f6e616c486561646572.29#/upload/video/frame")
    sleep(3)
   
    # 开始上传B站
    iframe=browser.find_element_by_xpath("//iframe[@name='videoUpload']")
    browser.switch_to_frame(iframe)
    browser.find_element_by_xpath("//input[@name='buploader']").send_keys(videoBean.videoPath)
    sleep(3)
    browser.find_element_by_xpath("//div[@class='cover-v2-preview']/input").send_keys(videoBean.picPath)
    sleep(2)
    browser.find_element_by_xpath("//div[@class='cover-chop-modal-v2-foot']/div").click()
    sleep(3)
    browser.find_element_by_xpath("//div[@class='select-box-v2-controller']").click()
    sleep(1)
    browser.find_element_by_xpath("//div[@class='drop-cascader-list-item']").click()
    sleep(1)
    tag=browser.find_element_by_xpath("//div[@class='content-tag-v2-input-wrp']//input")
    tag.send_keys("体育")
    tag.send_keys(Keys.ENTER)
    sleep(1)
    tag.send_keys("羽毛球")
    tag.send_keys(Keys.ENTER)
    sleep(1)
    tag.send_keys("赛事")
    tag.send_keys(Keys.ENTER)
    wait.until(lambda driver: browser.find_element_by_xpath("//i[@class='icon-success-v2']"))
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(1)
    browser.find_element_by_xpath("//span[@class='submit-btn-group-add']").click()
    print("B站上传成功")

# 爱奇艺
def uploadIqiyi(videoBean):
    wait = ui.WebDriverWait(browser, 600)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://mp.iqiyi.com/wemedia/publish/video")
    sleep(3)
    browser.find_element_by_xpath("//input").send_keys(videoBean.videoPath)
    sleep(8)
    browser.find_element_by_xpath("//input[@class='mp-upload__input']").send_keys(videoBean.picPath)
    sleep(2)
    browser.find_element_by_xpath("//input[@placeholder='选择分类']").click()
    sleep(1)
    browser.find_element_by_xpath("//span[text()='体育']/..").click()
    sleep(1)
    tag=browser.find_element_by_xpath("//div[@class='mp-input__multiple mp-input--tag']/input")
    tag.send_keys("体育")
    tag.send_keys(Keys.ENTER)
    sleep(1)
    tag.send_keys("羽毛球")
    tag.send_keys(Keys.ENTER)
    sleep(1)
    tag.send_keys("赛事")
    tag.send_keys(Keys.ENTER)
    browser.find_element_by_xpath("//span[@class='mp-radio__label']").click()
    wait.until(lambda driver: browser.find_element_by_xpath("//div[@class='ai-pro']"))
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(1)
    browser.find_element_by_xpath("//button[@class='mp-button mp-button--success is-animate']").click()
    print("爱奇艺上传成功")

# 一点号
def uploadYIDian(videoBean):
    wait = ui.WebDriverWait(browser, 600)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://mp.yidianzixun.com/#/Writing/videoEditor")
    sleep(3)
    browser.find_element_by_xpath("//input").send_keys(videoBean.videoPath)
    sleep(4)
    browser.find_element_by_xpath("//input[@class='cascader-input']").click()
    sleep(1)
    browser.find_element_by_xpath("//li[@title='体育']").click()
    sleep(1)
    browser.find_element_by_xpath("//div[@class='cover-container']").click()
    sleep(1)
    browser.find_element_by_xpath("//div[text()='本地上传      ']").click()
    sleep(1)
    browser.find_element_by_xpath("//div[@class='mp-uploader-container cover-border']//input").send_keys(videoBean.picPath)
    sleep(6)
    browser.find_element_by_xpath("//div[@class='confirm-btn btn-box']").click()
    sleep(3)
    wait.until(lambda driver: browser.find_element_by_xpath("//span[@class='mp-success']"))
    sleep(1)
    browser.find_element_by_xpath("//button[@class='mp-btn mp-btn-large mp-btn-primary']").click()
    sleep(1)
    browser.find_element_by_xpath("//div[@class='btn-container']/button[@class='mp-btn mp-btn-primary mp-btn-large']").click()
    print("一点号上传成功")

# 搜狐号
def uploadSohu(videoBean):
    wait = ui.WebDriverWait(browser, 600)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("https://mp.sohu.com/mpfe/v3/main/news/addvideo")
    sleep(3)
    browser.find_element_by_xpath("//input[@name='video']").send_keys(videoBean.videoPath)
    sleep(3)
    browser.find_element_by_xpath("//input[@id='crop-upload-file']").send_keys(videoBean.picPath)
    sleep(6)
    browser.find_element_by_xpath("//button[@class='sure-btn']").click()
    sleep(5)
    browser.find_element_by_xpath("//span[text()='请选择']").click()
    sleep(1)
    browser.find_element_by_xpath("//li[text()='羽毛球']").click()
    sleep(1)
    wait.until(lambda driver: browser.find_element_by_xpath("//p[@class='upload-tip upload-success']"))
    sleep(1)
    browser.find_element_by_xpath("//textarea[@class='abstract-textarea']").send_keys(browser.find_element_by_xpath("//input[@class='titleErrorInput']").get_attribute('value'))
    browser.find_element_by_xpath("//span[text()='发布']").click()
    print("搜狐号上传成功")

# 网易号
def upload163(videoBean):
    wait = ui.WebDriverWait(browser, 600)  # 10秒内每隔500毫秒扫描1次页面变化
    browser.execute_script('window.open()')
    browser.switch_to_window(browser.window_handles[len(browser.window_handles)-1])
    browser.get("http://mp.163.com/index.html#/post/video?wemediaId=W754906828151472311")
    sleep(3)   
    browser.find_element_by_xpath("//input").send_keys(videoBean.videoPath)
    sleep(3)
    browser.find_element_by_xpath("//div[@class='ne-input-mask-content']").click()
    sleep(1)
    browser.find_element_by_xpath("//input[@class='ne-input']").send_keys("羽毛球")
    sleep(1)
    browser.find_element_by_xpath("//span[text()='体育/羽毛球']").click()
    sleep(1)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    sleep(1)
    browser.find_element_by_xpath("//span[@class='ne-tag ne-tag-medium ne-tag-create']").click()
    sleep(1)
    ActionChains(browser).send_keys("体育").perform()
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    sleep(1)
    ActionChains(browser).send_keys("羽毛球").perform()
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    sleep(1)
    ActionChains(browser).send_keys("赛事").perform()
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    browser.find_element_by_xpath("//input[@class='cropper-input']").send_keys(videoBean.picPath)
    sleep(1)
    browser.find_element_by_xpath("//div[@class='column']/button[@class='ne-btn ne-btn-primary ne-btn-medium']").click()
    sleep(6)
    wait.until(lambda driver: browser.find_element_by_xpath("//div[@class='row info']/div[@class='column']"))
    browser.find_element_by_xpath("//button[@class='ne-btn ne-btn-primary ne-btn-medium form-submit-btn']").click()
    sleep(2)
    browser.find_element_by_xpath("//button[@class='ne-btn ne-btn-medium ne-btn-hollow']").click()
    print("网易号上传成功")
def onPublishVideo(videoBean):
        print(videoBean.title)
        print(videoBean.desc)
        print(videoBean.videoPath)
        print(videoBean.picPath)
        uploadTaoTiao(videoBean)
        uploadBaiJiaHao(videoBean)
        uploadDaYu(videoBean)
        uploadIqiyi(videoBean)
        uploadYIDian(videoBean)
        uploadSohu(videoBean)
        uploadBilibili(videoBean)
        uploadQiE(videoBean)
        # upload163(videoBean)
        



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
    
    






