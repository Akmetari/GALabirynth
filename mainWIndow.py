import sys

from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.initUI()

    def initUI(self):
        self.resize(875, 485)

        self.setMenu()
        self.setButtons()
        self.setDataFrame()
        self.setParamLabelsAndValues()

        self.labirynthFrame = QFrame(self)
        self.labirynthFrame.setGeometry(QRect(40, 50, 411, 321))
        self.labirynthFrame.setStyleSheet(u"    padding: 20px;\n"
                                          "    background-color: #ffffff;\n"
                                          "    border-radius: 15px;\n"
                                          "    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);\n"
                                          "    transition: transform 0.3s ease, box-shadow 0.3s ease;\n"
                                          "    overflow: hidden;")
        self.labirynthFrame.setFrameShape(QFrame.StyledPanel)
        self.labirynthFrame.setFrameShadow(QFrame.Raised)
        self.labirynthLabel = QLabel(self.labirynthFrame)
        self.labirynthLabel.setGeometry(QRect(20, 20, 371, 281))
        self.labirynthLabel.setAlignment(Qt.AlignCenter)



    def setButtons(self):
        self.startButton = QPushButton(self)
        self.startButton.setText("Start")
        self.startButton.setGeometry(QRect(100, 400, 101, 41))
        self.startButton.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0.389, y1:0.511, x2:0.383, y2:0, stop:0 rgba(138, 223, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "\n"
            "border-color: rgb(85, 170, 255);")

        # stop button
        self.stopButton = QPushButton(self)
        self.stopButton.setText("Stop")
        self.stopButton.setGeometry(QRect(260, 400, 101, 41))
        self.stopButton.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0.389, y1:0.511, x2:0.383, y2:0, stop:0 rgba(138, 223, 255, 255), stop:1 rgba(255, 255, 255, 255))")
    def setMenu(self):
        self.selectFromFileMenu = QAction(self)
        self.selectFromFileMenu.setText("selectFromFileMenu")
        self.createNewMenu = QAction(self)
        self.createNewMenu.setText("createNewMenu")
        self.setParametersMenu = QAction(self)
        self.setParametersMenu.setText("setParametersMenu")
        self.setLogDestinationMenu = QAction(self)
        self.setLogDestinationMenu.setText("setLogDestinationMenu")

        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        self.menuLabirynth = QMenu(self.menuBar)
        self.menuLabirynth.setTitle("Labirynth")
        self.menuAlgorithm = QMenu(self.menuBar)
        self.menuAlgorithm.setTitle("Algorithm")
        self.helpMenu = QMenu(self.menuBar)
        self.helpMenu.setTitle("Help")
        self.helpMenu.setBaseSize(QSize(0, 4))

        self.menuLabirynth.addAction(self.selectFromFileMenu)
        self.menuLabirynth.addAction(self.createNewMenu)
        self.menuAlgorithm.addAction(self.setParametersMenu)
        self.menuAlgorithm.addAction(self.setLogDestinationMenu)

        self.menuBar.addAction(self.menuLabirynth.menuAction())
        self.menuBar.addAction(self.menuAlgorithm.menuAction())
        self.menuBar.addAction(self.helpMenu.menuAction())

        self.menuBar.setStyleSheet(
            u"background-color: qlineargradient(spread:pad, x1:0.389, y1:0.511, x2:0.383, y2:0, stop:0 rgba(138, 223, 255, 255), stop:1 rgba(255, 255, 255, 255))\n"
            "")
    def setDataFrame(self):
        self.dataFrame = QFrame(self)
        self.dataFrame.setGeometry(QRect(510, 50, 331, 391))
        self.dataFrame.setStyleSheet(u"    padding: 20px;\n"
                                     "    background-color: #ffffff;\n"
                                     "    border-radius: 15px;\n"
                                     "    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);\n"
                                     "    transition: transform 0.3s ease, box-shadow 0.3s ease;\n"
                                     "    overflow: hidden;")
    def setParamLabelsAndValues(self):
        self.param1Label = QLabel(self.dataFrame)
        self.param1Label.setText("Cross chance: ")
        self.param1Label.setGeometry(QRect(20, 40, 120, 21))
        self.param1Label.setStyleSheet(u"    padding: 20px;\n"
                                       "background-color: rgb(138, 223, 255);\n"
                                       "    border-radius: 5px;\n"
                                       "    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);\n"
                                       "    transition: transform 0.3s ease, box-shadow 0.3s ease;\n"
                                       "    overflow: hidden;")

        self.param2Label = QLabel(self.dataFrame)
        self.param2Label.setText("Mute chance: ")
        self.param2Label.setGeometry(QRect(20, 99, 120, 21))
        self.param2Label.setStyleSheet(u"    padding: 20px;\n"
                                       "background-color: rgb(138, 223, 255);\n"
                                       "    border-radius: 5px;\n"
                                       "    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);\n"
                                       "    transition: transform 0.3s ease, box-shadow 0.3s ease;\n"
                                       "    overflow: hidden;")

        self.param3Label = QLabel(self.dataFrame)
        self.param3Label.setText("Pop size: ")
        self.param3Label.setGeometry(QRect(20, 159, 120, 21))
        self.param3Label.setStyleSheet(u"    padding: 20px;\n"
                                       "background-color: rgb(138, 223, 255);\n"
                                       "    border-radius: 5px;\n"
                                       "    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);\n"
                                       "    transition: transform 0.3s ease, box-shadow 0.3s ease;\n"
                                       "    overflow: hidden;")

        self.param1Value = QLabel(self.dataFrame)
        self.param1Value.setGeometry(QRect(200, 40, 101, 20))

        self.param2Value = QLabel(self.dataFrame)
        self.param2Value.setGeometry(QRect(190, 100, 131, 16))

        self.param3Value = QLabel(self.dataFrame)
        self.param3Value.setGeometry(QRect(190, 160, 121, 16))
def window():
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    sys.exit(app.exec_())


window()