import GUI.guiFormats as guiFormats
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class LogSettingsWindow(QWidget):

    def __init__(self, parent=None):
        super(LogSettingsWindow,self).__init__()
        self.initUI()
        self.parent=parent
    def initUI(self):
        self.resize(400, 200)

        self.pathLine = QLineEdit(self)
        self.pathLine.setGeometry(QRect(10, 100, 251, 31))

        self.setButtons()
        self.setTitles()

    def browse(self):
        self.fileDialog = QFileDialog(self)
        fName = self.fileDialog.getOpenFileName(self, "Browse", self.parent.data.logDir, "Text files (*.txt)")
        self.pathLine.setText(fName[0])

    def setButtons(self):
        self.setButton = QPushButton(self)
        self.setButton.setText("Set")
        self.setButton.setGeometry(QRect(150, 160, 111, 31))
        self.setButton.setStyleSheet(guiFormats.buttonStyle)

        self.browseButton = QPushButton(self)
        self.browseButton.setText("Browse")
        self.browseButton.setGeometry(QRect(290, 100, 93, 28))
        self.browseButton.setStyleSheet(guiFormats.buttonStyle)

        self.browseButton.clicked.connect(self.browse)

    def setCheckBoxes(self):
        self.logGenerationsBox = QCheckBox(self)
        self.logGenerationsBox.setText("Log generations")
        self.logGenerationsBox.setGeometry(QRect(40, 80, 121, 20))

        self.logStatsBox = QCheckBox(self)
        self.logStatsBox.setText("Log statistic data")
        self.logStatsBox.setGeometry(QRect(40, 120, 121, 20))

        self.printLogsBox = QCheckBox(self)
        self.printLogsBox.setText("Ready-to-print box")
        self.printLogsBox.setGeometry(QRect(210, 80, 141, 20))


    def setTitles(self):
        self.title2 = QLabel(self)
        self.title2.setText("Choose logging destination")
        self.title2.setGeometry(QRect(0, 20, 401, 31))
        self.title2.setStyleSheet(guiFormats.labelStyle)
        self.title2.setAlignment(Qt.AlignCenter)

