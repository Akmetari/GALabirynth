"""
Main view class. GUI includes all windows of gui with function managing them (eg. show) and data object that stores paarameters
that are being exchanged between view and controler.
It implements subject in observer pattern to notify Controler about users actions.

ActionType is an enumeration class that defines signals used to inform controller (throught observer pattern) about actions chosen by user.
"""
import sys
from PyQt5.QtWidgets import QApplication
from GUI.helpWindow import HelpWindow
from GUI.mainWindow import MainWindow
from GUI.getLabDataWindow import LabDataWindow
from GUI.paramSetWindow import ParamSetWindow
from GUI.createLabirynthWindow import CreateLabWindow
from GUI.logSettingsWindow import LogSettingsWindow
from GUI.getLabFromFileWindow import LabFromFileWindow
from GUI.popup import PopUp
from GUI.subject import Subject
from enum import Enum
from data import Data

class ActionType(Enum):
    setLog= 1,
    run = 2,
    stop = 3,
    setParam = 4,
    getLab = 5,
    createLab = 6



class GUI(Subject):
    def __init__(self):
        Subject.__init__(self)

        self.app = QApplication(sys.argv)
        self.data=Data()

        self.mainWindow: MainWindow =MainWindow(self)
        self.helpWindow: HelpWindow =HelpWindow(self)
        self.labDataWindow: LabDataWindow =LabDataWindow(self)
        self.paramSetWindow: ParamSetWindow =ParamSetWindow(self)
        self.createLabWindow: CreateLabWindow = CreateLabWindow(self)
        self.logSettings: LogSettingsWindow = LogSettingsWindow(self)
        self.getLabWindow: LabFromFileWindow = LabFromFileWindow(self)

        self.connectButtons()



    def appRun(self):
        self.mainWindow.show()
        sys.exit(self.app.exec_())

    def showHelp(self):
        self.helpWindow.show()
    def showLabData(self):
        self.labDataWindow.show()
    def showParamSet(self):
        self.paramSetWindow.show()
    def infoPopUp(self, text:str):
        self.popup=PopUp(text)
        self.popup.show()
    def showLabCreate(self):
        self.createLabWindow.show()
    def showLogSettings(self):
        self.logSettings.show()

    def showGetLabWindow(self):
        self.getLabWindow.show()

    def notifyRun(self):
        self.notify(ActionType.run)

    def notifyStop(self):
        self.notify(ActionType.stop)

    def notifySetLog(self):
        self.notify(ActionType.setLog)
        self.logSettings.close()

    def notifySetParam(self):
        self.notify(ActionType.setParam)
        self.paramSetWindow.close()

    def notifyCreateLab(self):
        self.notify(ActionType.createLab)
        self.createLabWindow.close()

    def notifyGetLab(self):
        self.notify(ActionType.getLab)
        self.getLabWindow.close()

    def connectButtons(self): #connects gui buttons with controler functions
        self.mainWindow.startButton.clicked.connect(self.notifyRun)
        self.mainWindow.stopButton.clicked.connect(self.notifyStop)

        self.logSettings.setButton.clicked.connect(self.notifySetLog)

        self.paramSetWindow.setButton.clicked.connect(self.notifySetParam)
        self.labDataWindow.createButton.clicked.connect(self.showLabCreate)
        self.labDataWindow.createButton.clicked.connect(self.labDataWindow.close)

        self.getLabWindow.loadFileButton.clicked.connect(self.notifyGetLab)

        self.createLabWindow.createButton.clicked.connect(self.notifyCreateLab)

        self.mainWindow.setParametersMenu.triggered.connect(self.showParamSet)
        self.mainWindow.createNewMenu.triggered.connect(self.showLabData)
        self.mainWindow.selectFromFileMenu.triggered.connect(self.showGetLabWindow)
        self.mainWindow.setLogDestinationMenu.triggered.connect(self.showLogSettings)
        self.mainWindow.helpMenu.triggered.connect(self.showHelp)

    def enable(self):
        self.mainWindow.menuAlgorithm.setEnabled(True)
        self.mainWindow.selectFromFileMenu.setEnabled(True)
        self.mainWindow.createNewMenu.setEnabled(True)
        self.mainWindow.startButton.setEnabled(True)
    def disable(self):
        self.mainWindow.menuAlgorithm.setEnabled(False)
        self.mainWindow.selectFromFileMenu.setEnabled(False)
        self.mainWindow.createNewMenu.setEnabled(False)
        self.mainWindow.startButton.setEnabled(False)

    def refresh(self):
        self.mainWindow.param1Value.setText(str(self.data.algParams[0]))
        self.mainWindow.param2Value.setText(str(self.data.algParams[1]))
        self.mainWindow.param3Value.setText(str(round(self.data.algParams[2])))
        self.mainWindow.param4Value.setText(str(round(self.data.algParams[3])))
        self.mainWindow.update()






