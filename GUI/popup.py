from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import GUI.guiFormats as guiFormats



class PopUp(QWidget):
    def __init__(self, text:str, parent=None):
        super(PopUp,self).__init__()
        self.setupUi(text)
        self.parent=parent
    def setupUi(self, text:str):
        self.setFixedSize(400, 137)
        self.okButton = QPushButton(self)
        self.okButton.setText("Ok")
        self.okButton.setGeometry(QRect(30, 90, 211, 31))
        self.okButton.setStyleSheet(guiFormats.buttonStyle)
        self.okButton.clicked.connect(self.close)

        self.label = QLabel(self)
        self.label.setText(text)
        self.label.setGeometry(QRect(-10, 30, 411, 51))
        self.label.setStyleSheet(guiFormats.smolLabelStyle)
        self.label.setAlignment(Qt.AlignCenter)