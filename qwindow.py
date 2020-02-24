#这里我们提供必要的引用。基本控件位于pyqt5.qtwidgets模块中。
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QFileDialog,QHBoxLayout,QVBoxLayout,QLineEdit
import sys
from videobean import VideoBean
class Qwindow(QWidget):
    def __init__(self,onPublishVideo):
        self.videoBean=VideoBean()
        self.onPublishVideo=onPublishVideo
        super().__init__()
        self.initUI()
        
    def initUI(self):
        vbox=QVBoxLayout()

        videoBox=QHBoxLayout()
        btnVideo = QPushButton('选择视频')
        btnVideo.clicked.connect(self.showVideoDialog)
        self.labelVideo=QLabel()
        videoBox.addWidget(btnVideo)
        videoBox.addWidget(self.labelVideo)
        videoBox.addStretch(1)
        vbox.addLayout(videoBox)

        picBox=QHBoxLayout()
        btnPic = QPushButton('设置封面')
        btnPic.clicked.connect(self.showPicDialog)
        self.labelPic=QLabel()
        picBox.addWidget(btnPic)
        picBox.addWidget(self.labelPic)
        picBox.addStretch(1)
        vbox.addLayout(picBox)

        titleBox=QHBoxLayout()
        self.titleEidt=QLineEdit()
        titleBox.addWidget(QLabel("标题"))
        titleBox.addWidget(self.titleEidt)
    
        vbox.addLayout(titleBox)

        descBox=QHBoxLayout()
        self.descEdit=QLineEdit()
        descBox.addWidget(QLabel("描述"))
        descBox.addWidget(self.descEdit)
     
        vbox.addLayout(descBox)

        btnRelease = QPushButton('发布')
        btnRelease.clicked.connect(self.release)
        vbox.addWidget(btnRelease)

        self.setLayout(vbox)
        self.resize(600,400)
        self.setWindowTitle("自媒体多平台发布系统")
        self.show()

    def showVideoDialog(self):
        fname=QFileDialog.getOpenFileName(self,"选择文件")
        if fname[0]:
            self.labelVideo.setText(fname[0])
            self.videoBean.videoPath=fname[0]
        

    def showPicDialog(self):
        fname=QFileDialog.getOpenFileName(self,"选择文件")
        if fname[0]:
            self.labelPic.setText(fname[0])
            self.videoBean.picPath=fname[0]

    def release(self):
        self.videoBean.title=self.titleEidt.text()
        self.videoBean.desc=self.descEdit.text()
        # print(self.videoBean.title)
        # print(self.videoBean.desc)
        # print(self.videoBean.videoPath)
        # print(self.videoBean.picPath)
        self.onPublishVideo(self.videoBean)
        pass



if __name__ == "__main__":
    def onPublishVideo(videoBean):
        print(videoBean.title)
        print(videoBean.desc)
        print(videoBean.videoPath)
        print(videoBean.picPath)   
    app=QApplication(sys.argv)
    ex=Qwindow(onPublishVideo)

    sys.exit(app.exec_())

