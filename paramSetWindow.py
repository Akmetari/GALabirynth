from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class ParamSetWindow(QWidget):

    frameStyle: str = u"padding: 20px;\nbackground-color: #ffffff;\nborder-radius: 15px;\nbox-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);\ntransition: transform 0.3s ease, box-shadow 0.3s ease;\noverflow: hidden;"
    labelStyle: str = u"background-color: rgb(138, 223, 255);\nfont-size: 20px;"
    buttonStyle: str = u"background-color: qlineargradient(spread:pad, x1:0.389, y1:0.511, x2:0.383, y2:0, stop:0 rgba(138, 223, 255, 255), stop:1 rgba(255, 255, 255, 255));\nborder-color: rgb(85, 170, 255);"
    def __init__(self, paramNames: dict[str,(float,float,float)]= {"Cross chance": (60.0,0.0,100.0), "Mutation chance": (0.001,0.0,100.0), "Pop size": (10.0,10.0,100000.0)}):
        super(ParamSetWindow, self).__init__()
        self.initUI(paramNames)

    def initUI(self, params: dict):
        self.resize(250, 260)

        self.setTitleLabel()
        self.setParamsLabels(list(params.keys()))
        self.setParamValues(list(params.values()))



    def setTitleLabel(self):
        self.setParamsLabel = QLabel(self)
        self.setParamsLabel.setText("Set parameters")
        self.setParamsLabel.setGeometry(QRect(0, 40, 251, 51))
        self.setParamsLabel.setStyleSheet(self.labelStyle)
        self.setParamsLabel.setAlignment(Qt.AlignCenter)

    def setParamsLabels(self, paramNames: list[str]):
        i: int=0
        self.params: list[QLabel]=[]

        for name in paramNames:
            label=QLabel(self)
            label.setText(name+ ": ")
            label.setGeometry(QRect(10, 160+(i*40), 141, 21))
            label.setStyleSheet(self.labelStyle)
            self.params.append(label)
            i+=1

    def setParamValues(self, paramValues: list[(float,float,float)]):
        i: int = 0
        self.paramValues: list[QDoubleSpinBox] = []

        for valueTuple in paramValues:
            box = QDoubleSpinBox(self)
            val=valueTuple[0]
            min=valueTuple[1]
            max=valueTuple[2]
            box.setValue(val)
            box.setMaximum(max)
            box.setMinimum(min)
            box.setGeometry(QRect(10, 160 + (i * 40), 141, 21))
            self.paramValues.append(box)
            i += 1