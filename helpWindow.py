from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class HelpWindow(QWidget):

    helpText:str="help text"
    frameStyle: str=u"padding: 20px;\nbackground-color: #ffffff;\nborder-radius: 15px;\nbox-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);\ntransition: transform 0.3s ease, box-shadow 0.3s ease;\noverflow: hidden;"
    labelStyle :str=u"background-color: rgb(138, 223, 255);\nfont-size: 20px;"
    buttonStyle: str=u"background-color: qlineargradient(spread:pad, x1:0.389, y1:0.511, x2:0.383, y2:0, stop:0 rgba(138, 223, 255, 255), stop:1 rgba(255, 255, 255, 255));\nborder-color: rgb(85, 170, 255);"
    def __init__(self):
        super(HelpWindow, self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(454, 419)
        self.setLabel()
        self.setOkButton()
        self.setHelpFrame()
        self.setText(self.helpText)

    def setHelpFrame(self):
        self.helpFrame = QFrame(self)
        self.helpFrame.setGeometry(QRect(20, 100, 411, 251))
        self.helpFrame.setStyleSheet(self.frameStyle)
        self.helpFrame.setFrameShape(QFrame.StyledPanel)
        self.helpFrame.setFrameShadow(QFrame.Raised)

    def setText(self,text: str):
        self.helpTextLabel = QLabel(self.helpFrame)
        self.helpTextLabel.setText(text)
        self.helpTextLabel.setGeometry(QRect(20, 20, 361, 211))
        self.helpTextLabel.setAlignment(Qt.AlignCenter)
    def setOkButton(self):
        self.okButton = QPushButton(self)
        self.okButton.setText("Ok")
        self.okButton.setGeometry(QRect(170, 360, 101, 41))
        self.okButton.setStyleSheet(self.buttonStyle)


    def setLabel(self):
        self.helpLabel = QLabel(self)
        self.helpLabel.setText("Help")
        self.helpLabel.setGeometry(QRect(0, 29, 461, 51))
        self.helpLabel.setStyleSheet(self.labelStyle)
        self.helpLabel.setAlignment(Qt.AlignCenter)