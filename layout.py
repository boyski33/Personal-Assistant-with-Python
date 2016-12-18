import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QGroupBox, QDialog, QVBoxLayout
from PyQt5.QtCore import pyqtSlot
 
class App(QDialog):
 
    def __init__(self):
        super(App, self).__init__()
        self.title = 'OK, Hacker!'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 100
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        self.createHorizontalLayout()
 
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
 
        self.show()
 
    def createHorizontalLayout(self):
        
        self.horizontalGroupBox = QGroupBox()
        layout = QVBoxLayout()
        
        
        settingsb = QPushButton('Settings', self)
        settingsb.setCheckable(False)
        settingsb.setStyleSheet("background-color: grey")
        settingsb.clicked.connect(self.set_on_click)
        layout.addWidget(settingsb)
        
        pushToSpeak = QPushButton('Push And Talk', self)
        pushToSpeak.setCheckable(True)
        pushToSpeak.clicked.connect(self.on_click)
        pushToSpeak.setStyleSheet("background-color: grey")
        layout.addWidget(pushToSpeak) 
 
        self.horizontalGroupBox.setLayout(layout)

 
    @pyqtSlot()
    def on_click(self):
        print('button click')
        
    @pyqtSlot()
    def set_on_click(self):
        print("settings click")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
    