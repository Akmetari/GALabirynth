from PyQt5.QtCore import *

from PyQt5.QtWidgets import *
class CreateLabWindow(QWidget):
    buttonStyle: str = u"background-color: qlineargradient(spread:pad, x1:0.389, y1:0.511, x2:0.383, y2:0, stop:0 rgba(138, 223, 255, 255), stop:1 rgba(255, 255, 255, 255));\nborder-color: rgb(85, 170, 255);"
    labelStyle: str = u"background-color: rgb(138, 223, 255);\nfont-size: 20px;"
    def __init__(self, legend: list(str,str)):
        super(CreateLabWindow,self).__init__()
        self.initUI(legend)



    def initUI(self, legend):
        self.resize(534, 497)
        self.setLegend(legend)
        self.setCreateButton()
        self.setTitleLabel()

        self.labirynthCreateInput = QPlainTextEdit(self)
        self.labirynthCreateInput.setGeometry(QRect(20, 90, 391, 311))



    def setLegend(self, symbols: list[(str,str)]): # tuples of name and symbol representing different parts of labirynth
        self.wallLegend = QLabel(self)
        self.wallLegend.setText("Legend")
        self.wallLegend.setGeometry(QRect(420, 170, 51, 31))


        i: int =0
        for s in symbols:
            legendLabel = QLabel(self)
            legendLabel.setText(s[0])
            legendLabel.setGeometry(QRect(420, 200+i*20, 51, 31))

            legendValue = QLabel(self)
            legendValue.setText(s[1])
            legendValue.setGeometry(QRect(420, 200+i*20, 51, 31))

            i+=1

    def setCreateButton(self):
        self.createButton = QPushButton(self)
        self.createButton.setText("Create and save")
        self.createButton.setGeometry(QRect(160, 420, 131, 51))
        self.createButton.setStyleSheet(self.buttonStyle)

    def setTitleLabel(self):
        self.label = QLabel(self)
        self.label.setText("Create labirynth")
        self.label.setGeometry(QRect(0, 29, 541, 41))
        self.label.setStyleSheet(self.labelStyle)
        self.label.setAlignment(Qt.AlignCenter)