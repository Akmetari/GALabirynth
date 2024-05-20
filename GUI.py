import sys
from PyQt5.QtWidgets import QApplication
from mainWIndow import MainWindow
from helpWindow import HelpWindow
from getLabDataWindow import LabDataWindow
from paramSetWindow import ParamSetWindow

class GUI(object):
    def __init__(self):
        self.mainWindow=MainWindow()
        self.helpWindow=HelpWindow()
        self.labDataWindow=LabDataWindow()
        self.paramSetWindow=ParamSetWindow()
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