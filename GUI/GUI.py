import sys
from PyQt5.QtWidgets import QApplication
from mainWIndow import MainWindow
from helpWindow import HelpWindow
from getLabDataWindow import LabDataWindow
from paramSetWindow import ParamSetWindow
from createLabirynthWindow import CreateLabWindow
from logSettingsWindow import LogSettingsWindow
from popup import PopUp


from Control import Controler
class GUI(object):
    def __init__(self, controller:Controler):
        self.controller: Controler =controller
        self.controller.setGUI(self)

        self.mainWindow: MainWindow =MainWindow()
        self.helpWindow: HelpWindow =HelpWindow()
        self.labDataWindow: LabDataWindow =LabDataWindow()
        self.paramSetWindow: ParamSetWindow =ParamSetWindow()
        self.createLabWindow: CreateLabWindow = CreateLabWindow(controller.getLegend())
        self.logSettings: LogSettingsWindow = LogSettingsWindow()

        self.connectButtons()

        self.app = QApplication(sys.argv)

    def appRun(self):
        self.mainWindow.show()
        sys.exit(self.app.exec_())

    def showHelp(self):
        self.helpWindow.show()
    def showLabData(self):
        self.labDataWindow.show()
    def showParamSet(self):
        self.paramSetWindow.show()
    def infoPopUp(self, text):
        self.popup=PopUp(text)
        self.popup.show()

    def showLogSettings(self):
        self.logSettings.show()

    def connectButtons(self): #connects gui buttons with controler functions
        self.mainWindow.startButton.clicked.connect(self.controller.run())
        self.mainWindow.stopButton.clicked.connect(self.controller.stop())

        self.logSettings.browseButton.clicked.connect(self.controller.browse())
        self.logSettings.setButton.clicked.connect(self.controller.setLogSettings())

        self.paramSetWindow.setButton.clicked.connect(self.controller.setParams())
        self.labDataWindow.createButton.clicked.connect(self.controller.startCreateLab())

        self.createLabWindow.createButton.clicked.connect(self.controller.createLab())
