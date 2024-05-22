import GUI.guiFormats as guiFormats
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

    buttonsY:int =400
    buttonSizeX: int=101
    buttonSizeY: int=41

    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()


    def initUI(self):
        self.resize(875, 485)

        self.setMenu()
        self.setButtons()
        self.setDataFrame()
        self.setParamLabelsAndValues()

        self.labirynthFrame = QFrame(self)
        self.labirynthFrame.setGeometry(QRect(40, 50, 411, 321))
        self.labirynthFrame.setStyleSheet(guiFormats.frameStyle)
        self.labirynthFrame.setFrameShape(QFrame.StyledPanel)
        self.labirynthFrame.setFrameShadow(QFrame.Raised)
        self.labirynthLabel = QLabel(self.labirynthFrame)
        self.labirynthLabel.setGeometry(QRect(20, 20, 371, 281))
        self.labirynthLabel.setAlignment(Qt.AlignCenter)



    def setButtons(self):
        self.startButton = QPushButton(self)
        self.startButton.setText("Start")
        self.startButton.setGeometry(QRect(100, self.buttonsY, self.buttonSizeX, self.buttonSizeY))
        self.startButton.setStyleSheet(guiFormats.buttonStyle)

        # stop button
        self.stopButton = QPushButton(self)
        self.stopButton.setText("Stop")
        self.stopButton.setGeometry(QRect(260, self.buttonsY, self.buttonSizeX, self.buttonSizeY))
        self.stopButton.setStyleSheet(guiFormats.buttonStyle)
    def setMenu(self):
        self.selectFromFileMenu = QAction(self)
        self.selectFromFileMenu.setText(r"Select labirynth from file")
        self.createNewMenu = QAction(self)
        self.createNewMenu.setText("Create new labirynth")
        self.setParametersMenu = QAction(self)
        self.setParametersMenu.setText("Set parameters")
        self.setLogDestinationMenu = QAction(self)
        self.setLogDestinationMenu.setText("Set log destination")

        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        self.menuLabirynth = QMenu(self.menuBar)
        self.menuLabirynth.setTitle("Labirynth")
        self.menuAlgorithm = QMenu(self.menuBar)
        self.menuAlgorithm.setTitle("Algorithm")
        self.helpMenu = QAction(self.menuBar)
        self.helpMenu.setText("Help")

        self.menuLabirynth.addAction(self.selectFromFileMenu)
        self.menuLabirynth.addAction(self.createNewMenu)
        self.menuAlgorithm.addAction(self.setParametersMenu)
        self.menuAlgorithm.addAction(self.setLogDestinationMenu)

        self.menuBar.addAction(self.menuLabirynth.menuAction())
        self.menuBar.addAction(self.menuAlgorithm.menuAction())
        self.menuBar.addAction(self.helpMenu)

        self.menuBar.setStyleSheet(guiFormats.menuStyle)
    def setDataFrame(self):
        self.dataFrame = QFrame(self)
        self.dataFrame.setGeometry(QRect(510, 50, 331, 391))
        self.dataFrame.setStyleSheet(guiFormats.frameStyle)
    def setParamLabelsAndValues(self):
        self.param1Label = QLabel(self.dataFrame)
        self.param1Label.setText("Cross chance: ")
        self.param1Label.setGeometry(QRect(20, 40, 120, 21))
        self.param1Label.setStyleSheet(guiFormats.labelStyle)

        self.param2Label = QLabel(self.dataFrame)
        self.param2Label.setText("Mute chance: ")
        self.param2Label.setGeometry(QRect(20, 99, 120, 21))
        self.param2Label.setStyleSheet(guiFormats.labelStyle)

        self.param3Label = QLabel(self.dataFrame)
        self.param3Label.setText("Pop size: ")
        self.param3Label.setGeometry(QRect(20, 159, 120, 21))
        self.param3Label.setStyleSheet(guiFormats.labelStyle)

        self.param1Value = QLabel(self.dataFrame)
        self.param1Value.setGeometry(QRect(200, 40, 101, 20))

        self.param2Value = QLabel(self.dataFrame)
        self.param2Value.setGeometry(QRect(190, 100, 131, 16))

        self.param3Value = QLabel(self.dataFrame)
        self.param3Value.setGeometry(QRect(190, 160, 121, 16))

