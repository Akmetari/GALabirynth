from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class LabDataWindow(QWidget):
    labelStyle: str = u"background-color: rgb(138, 223, 255);\nfont-size: 20px;"
    buttonStyle: str = u"background-color: qlineargradient(spread:pad, x1:0.389, y1:0.511, x2:0.383, y2:0, stop:0 rgba(138, 223, 255, 255), stop:1 rgba(255, 255, 255, 255));\nborder-color: rgb(85, 170, 255);"
    def __init__(self):
        super(LabDataWindow, self).__init__()
        self.initUI()

    def initUI(self):

        self.resize(400, 300)
        self.setTitleLabel()
        self.setFileChoice()
        self.setSizeChoice()
        self.setSteeringButtons()


    def setFileChoice(self):
        self.setPathLine()
        self.setBrowseButton()
    def setPathLine(self):
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QRect(20, 91, 221, 31))
    def setBrowseButton(self):
        self.pushButton = QPushButton(self)
        self.pushButton.setText("Browse")
        self.pushButton.setGeometry(QRect(270, 90, 101, 31))
        self.pushButton.setStyleSheet(self.buttonStyle)

    def setTitleLabel(self):
        self.titleLabel = QLabel(self)
        self.titleLabel.setText("Set labyrinth size and location")
        self.titleLabel.setGeometry(QRect(0, 29, 401, 41))
        self.titleLabel.setStyleSheet(self.labelStyle)
        self.titleLabel.setAlignment(Qt.AlignCenter)


    def setSteeringButtons(self):
        self.startLabCreateButton = QPushButton(self)
        self.startLabCreateButton.setObjectName("Create")
        self.startLabCreateButton.setGeometry(QRect(60, 230, 101, 31))
        self.startLabCreateButton.setStyleSheet(self.buttonStyle)

        self.startLabCancelButton = QPushButton(self)
        self.startLabCancelButton.setText("Cancel")
        self.startLabCancelButton.setGeometry(QRect(220, 230, 101, 31))
        self.startLabCancelButton.setStyleSheet(self.buttonStyle)

    def setSizeChoice(self):
        self.xSizeLabel = QLabel(self)
        self.xSizeLabel.setGeometry(QRect(30, 160, 81, 21))
        self.xSizeLabel.setStyleSheet(self.labelStyle)

        self.ySizeLabel = QLabel(self)
        self.ySizeLabel.setGeometry(QRect(220, 160, 81, 21))
        self.ySizeLabel.setStyleSheet(self.labelStyle)

        self.xSizeBox = QSpinBox(self)
        self.xSizeBox.setGeometry(QRect(130, 160, 42, 22))
        self.xSizeBox.setMinimum(1)
        self.xSizeBox.setMaximum(100)

        self.ySizeBox = QSpinBox(self)
        self.ySizeBox.setGeometry(QRect(320, 160, 42, 22))
        self.ySizeBox.setMinimum(1)
        self.ySizeBox.setMaximum(100)


