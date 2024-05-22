from PyQt5.QtCore import *
import GUI.guiFormats as guiFormats
from PyQt5.QtWidgets import *
class CreateLabWindow(QWidget):
    def __init__(self ):
        super(CreateLabWindow,self).__init__()
        self.initUI()



    def initUI(self):
        self.resize(534, 497)
        self.setLegend()
        self.setCreateButton()
        self.setTitleLabel()

        self.labirynthCreateInput = QPlainTextEdit(self)
        self.labirynthCreateInput.setGeometry(QRect(20, 90, 391, 311))



    def setLegend(self, symbols: list[(str,str)] = [("Wall","9"),("Empty","0"), ("Right","1"),("Left","3"), ("Up","2"), ("Down","4")]): # tuples of name and symbol representing different parts of labirynth
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
        self.createButton.setStyleSheet(guiFormats.buttonStyle)

    def setTitleLabel(self):
        self.label = QLabel(self)
        self.label.setText("Create labirynth")
        self.label.setGeometry(QRect(0, 29, 541, 41))
        self.label.setStyleSheet(guiFormats.labelStyle)
        self.label.setAlignment(Qt.AlignCenter)