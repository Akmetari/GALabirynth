from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class PopUp(QWidget):
    labelStyle: str = u"background-color: rgb(138, 223, 255);\nfont-size: 20px;"
    buttonStyle: str = u"background-color: qlineargradient(spread:pad, x1:0.389, y1:0.511, x2:0.383, y2:0, stop:0 rgba(138, 223, 255, 255), stop:1 rgba(255, 255, 255, 255));\nborder-color: rgb(85, 170, 255);"
    def __init__(self, text):
        super(PopUp,self).__init__()
        self.setupUi(text)
    def setupUi(self, text):
        self.resize(400, 137)
        self.okButton = QPushButton(self)
        self.okButton.setText("Ok")
        self.okButton.setGeometry(QRect(30, 90, 211, 31))
        self.okButton.setStyleSheet(self.buttonStyle)

        self.label = QLabel(self)
        self.label.setText(text)
        self.label.setGeometry(QRect(-10, 30, 411, 51))
        self.label.setStyleSheet(self.labelStyle)
        self.label.setAlignment(Qt.AlignCenter)