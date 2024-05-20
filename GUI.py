import sys
from PyQt5.QtWidgets import QApplication
from mainWIndow import MainWindow

class GUI(object):
    def __init__(self):
        self.mainWindow=MainWindow()
        self.app = QApplication(sys.argv)

    def appRun(self):
        self.mainWindow.show()
        sys.exit(self.app.exec_())