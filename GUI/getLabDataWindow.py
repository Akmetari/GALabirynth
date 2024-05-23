from PyQt5.QtCore import *
import GUI.guiFormats as guiFormats
from PyQt5.QtWidgets import *


class LabDataWindow(QWidget):
    def __init__(self, parent=None):
        super(LabDataWindow, self).__init__()
        self.initUI()
        self.parent=parent


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

    def browse(self, path: str = "C:/"):
        self.fileDialog = QFileDialog(self)
        fName = self.fileDialog.getOpenFileName(self, "Browse", "D:/code", "Text files (*.txt)")
        self.lineEdit.setText(fName[0])
    def setBrowseButton(self):
        self.pushButton = QPushButton(self)
        self.pushButton.setText("Browse")
        self.pushButton.setGeometry(QRect(270, 90, 101, 31))
        self.pushButton.setStyleSheet(guiFormats.buttonStyle)
        self.pushButton.clicked.connect(self.browse)

    def setTitleLabel(self):
        self.titleLabel = QLabel(self)
        self.titleLabel.setText("Set labyrinth size and location")
        self.titleLabel.setGeometry(QRect(0, 29, 401, 41))
        self.titleLabel.setStyleSheet(guiFormats.labelStyle)
        self.titleLabel.setAlignment(Qt.AlignCenter)

    def exportData(self):
        self.parent.data.xSize=self.xSizeBox.value()
        self.parent.data.ySize=self.ySizeBox.value()
        self.parent.data.saveDir=self.lineEdit.text()


    def setSteeringButtons(self):
        self.createButton = QPushButton(self)
        self.createButton.setText("Create")
        self.createButton.setGeometry(QRect(60, 230, 101, 31))
        self.createButton.setStyleSheet(guiFormats.buttonStyle)
        self.createButton.clicked.connect(self.exportData)


        self.cancelButton = QPushButton(self)
        self.cancelButton.setText("Cancel")
        self.cancelButton.setGeometry(QRect(220, 230, 101, 31))
        self.cancelButton.setStyleSheet(guiFormats.buttonStyle)
        self.cancelButton.clicked.connect(self.close)

    def setSizeChoice(self):
        self.xSizeLabel = QLabel(self)
        self.xSizeLabel.setText("X size:")
        self.xSizeLabel.setGeometry(QRect(30, 160, 81, 21))
        self.xSizeLabel.setStyleSheet(guiFormats.smolLabelStyle)
        self.xSizeLabel.setAlignment(Qt.AlignCenter)

        self.ySizeLabel = QLabel(self)
        self.ySizeLabel.setText("Y size:")
        self.ySizeLabel.setGeometry(QRect(220, 160, 81, 21))
        self.ySizeLabel.setStyleSheet(guiFormats.smolLabelStyle)
        self.ySizeLabel.setAlignment(Qt.AlignCenter)

        self.xSizeBox = QSpinBox(self)
        self.xSizeBox.setGeometry(QRect(130, 160, 42, 22))
        self.xSizeBox.setMinimum(1)
        self.xSizeBox.setMaximum(100)

        self.ySizeBox = QSpinBox(self)
        self.ySizeBox.setGeometry(QRect(320, 160, 42, 22))
        self.ySizeBox.setMinimum(1)
        self.ySizeBox.setMaximum(100)


