import sys
from PyQt5.QtWidgets import QApplication
from mainWIndow import MainWindow
from helpWindow import HelpWindow
from getLabDataWindow import LabDataWindow
from paramSetWindow import ParamSetWindow
from createLabirynthWindow import CreateLabWindow
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