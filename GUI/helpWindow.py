from PyQt5.QtCore import *
import guiFormats
from PyQt5.QtWidgets import *

class HelpWindow(QWidget):

    helpText:str="help text"

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
        self.helpFrame.setStyleSheet(guiFormats.frameStyle)
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
        self.okButton.setStyleSheet(guiFormats.buttonStyle)

        self.okButton.clicked.connect(self.close())


    def setLabel(self):
        self.helpLabel = QLabel(self)
        self.helpLabel.setText("Help")
        self.helpLabel.setGeometry(QRect(0, 29, 461, 51))
        self.helpLabel.setStyleSheet(guiFormats.labelStyle)
        self.helpLabel.setAlignment(Qt.AlignCenter)