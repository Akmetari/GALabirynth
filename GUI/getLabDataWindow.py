from PyQt5.QtCore import *
import GUI.guiFormats as guiFormats
from PyQt5.QtWidgets import *

class LabDataWindow(QWidget):
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
        self.pushButton.setStyleSheet(guiFormats.buttonStyle)

    def setTitleLabel(self):
        self.titleLabel = QLabel(self)
        self.titleLabel.setText("Set labyrinth size and location")
        self.titleLabel.setGeometry(QRect(0, 29, 401, 41))
        self.titleLabel.setStyleSheet(guiFormats.labelStyle)
        self.titleLabel.setAlignment(Qt.AlignCenter)


    def setSteeringButtons(self):
        self.createButton = QPushButton(self)
        self.createButton.setObjectName("Create")
        self.createButton.setGeometry(QRect(60, 230, 101, 31))
        self.createButton.setStyleSheet(guiFormats.buttonStyle)

        self.cancelButton = QPushButton(self)
        self.cancelButton.setText("Cancel")
        self.cancelButton.setGeometry(QRect(220, 230, 101, 31))
        self.cancelButton.setStyleSheet(guiFormats.buttonStyle)
        self.cancelButton.clicked.connect(self.close)

    def setSizeChoice(self):
        self.xSizeLabel = QLabel(self)
        self.xSizeLabel.setGeometry(QRect(30, 160, 81, 21))
        self.xSizeLabel.setStyleSheet(guiFormats.labelStyle)

        self.ySizeLabel = QLabel(self)
        self.ySizeLabel.setGeometry(QRect(220, 160, 81, 21))
        self.ySizeLabel.setStyleSheet(guiFormats.labelStyle)

        self.xSizeBox = QSpinBox(self)
        self.xSizeBox.setGeometry(QRect(130, 160, 42, 22))
        self.xSizeBox.setMinimum(1)
        self.xSizeBox.setMaximum(100)

        self.ySizeBox = QSpinBox(self)
        self.ySizeBox.setGeometry(QRect(320, 160, 42, 22))
        self.ySizeBox.setMinimum(1)
        self.ySizeBox.setMaximum(100)


