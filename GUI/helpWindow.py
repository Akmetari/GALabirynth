from PyQt5.QtCore import *
import GUI.guiFormats as guiFormats
from PyQt5.QtWidgets import *

class HelpWindow(QWidget):

    helpText:str=("If you start algorithm without labirynth,it will run on a default one.\n"
                  "Pick labirynth: Labirynth -> Select labirynth from file\n"
                  "Create your own labirynth: Labirynth -> Create labirynth\n"
                  "Change algorithm or logging parameters: Algorithm menu.\n\n"
                  "App created by Alicja Huk")


    def __init__(self, parent =None):
        super(HelpWindow, self).__init__()
        self.initUI()
        self.parent=parent

    def initUI(self):
        self.setFixedSize(454, 419)
        self.setLabel()
        self.setOkButton()
        self.setHelpFrame()
        self.setText(self.helpText)

    def setHelpFrame(self):
        self.helpFrame = QFrame(self)
        self.helpFrame.setGeometry(QRect(20, 100, 411, 251))
        self.helpFrame.setStyleSheet(guiFormats.thinFrameStyle)

    def setText(self,text: str):
        self.helpTextLabel = QLabel(self.helpFrame)
        self.helpTextLabel.setGeometry(QRect(20, 20, 400, 200))
        self.helpTextLabel.setText(text)
        self.helpTextLabel.adjustSize()
        self.helpTextLabel.setAlignment(Qt.AlignLeft)
    def setOkButton(self):
        self.okButton = QPushButton(self)
        self.okButton.setText("Ok")
        self.okButton.setGeometry(QRect(170, 360, 101, 41))
        self.okButton.setStyleSheet(guiFormats.buttonStyle)

        self.okButton.clicked.connect(self.close)


    def setLabel(self):
        self.helpLabel = QLabel(self)
        self.helpLabel.setText("Help")
        self.helpLabel.setGeometry(QRect(0, 29, 461, 51))
        self.helpLabel.setStyleSheet(guiFormats.labelStyle)
        self.helpLabel.setAlignment(Qt.AlignCenter)