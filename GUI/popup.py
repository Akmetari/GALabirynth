from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import guiFormats

class PopUp(QWidget):
    def __init__(self, text):
        super(PopUp,self).__init__()
        self.setupUi(text)
    def setupUi(self, text):
        self.resize(400, 137)
        self.okButton = QPushButton(self)
        self.okButton.setText("Ok")
        self.okButton.setGeometry(QRect(30, 90, 211, 31))
        self.okButton.setStyleSheet(guiFormats.buttonStyle)

        self.label = QLabel(self)
        self.label.setText(text)
        self.label.setGeometry(QRect(-10, 30, 411, 51))
        self.label.setStyleSheet(guiFormats.labelStyle)
        self.label.setAlignment(Qt.AlignCenter)