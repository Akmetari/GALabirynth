from PyQt5.QtCore import *
import GUI.guiFormats as guiFormats
from PyQt5.QtWidgets import *

class ParamSetWindow(QWidget):
    def __init__(self, parent=None, paramNames: dict[str,(float,float,float)]= {"Cross chance": (60.0,0.0,100.0), "Mutation chance": (0.001,0.0,100.0), "Pop size": (10.0,10.0,100000.0)}):
        super(ParamSetWindow, self).__init__()
        self.initUI(paramNames)
        self.parent=parent

    def initUI(self, params: dict):
        self.resize(250, 300)

        self.setTitleLabel()
        self.setParamsLabels(list(params.keys()))
        self.setParamValues(list(params.values()))

        self.setButton = QPushButton(self)
        self.setButton.setText("Set")
        self.setButton.setGeometry(QRect(72, 250, 101, 31))



    def setTitleLabel(self):
        self.setParamsLabel = QLabel(self)
        self.setParamsLabel.setText("Set parameters")
        self.setParamsLabel.setGeometry(QRect(0, 40, 251, 51))
        self.setParamsLabel.setStyleSheet(guiFormats.labelStyle)
        self.setParamsLabel.setAlignment(Qt.AlignCenter)

    def setParamsLabels(self, paramNames: list[str]):
        i: int=0
        self.params: list[QLabel]=[]

        for name in paramNames:
            label=QLabel(self)
            label.setText(name+ ": ")
            label.setGeometry(QRect(10, 110+(i*40), 140, 25))
            label.setStyleSheet(guiFormats.smolLabelStyle)
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
            box.setGeometry(QRect(170, 110 + (i * 40), 60, 25))
            self.paramValues.append(box)
            i += 1