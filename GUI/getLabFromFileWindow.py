from PyQt5.QtCore import *
import GUI.guiFormats as guiFormats
from PyQt5.QtWidgets import *

class LabFromFileWindow(QWidget):
    def __init__(self):
        super(LabFromFileWindow,self).__init__()
        self.initUi()
    def initUi(self):

        self.resize(400, 173)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QRect(10, 80, 251, 31))

        self.setButtons()

        self.label = QLabel(self)
        self.label.setText("Choose labirynth file")
        self.label.setGeometry(QRect(0, 20, 401, 41))
        self.label.setStyleSheet(guiFormats.labelStyle)
        self.label.setAlignment(Qt.AlignCenter)


    def setButtons(self):
        self.browseButton = QPushButton(self)
        self.browseButton.setText("Browse")
        self.browseButton.setGeometry(QRect(290, 80, 93, 28))
        self.browseButton.setStyleSheet(guiFormats.buttonStyle)

        self.loadFileButton = QPushButton(self)
        self.loadFileButton.setText("Load file")
        self.loadFileButton.setGeometry(QRect(150, 127, 111, 31))
        self.loadFileButton.setStyleSheet(guiFormats.buttonStyle)