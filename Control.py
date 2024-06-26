"""
Controler class manages model and gui, controls data and app flow by running both gui and model methods.
It implements observer pattern whitch it uses to monitor user-view interactions.
"""


import copy
import datetime as dt
from datetime import datetime
import threading
from model.GA import GA
from GUI.GUI import GUI
from GUI.GUI import ActionType
from observer import  Observer

class Controler(Observer):

    def __init__(self, newGUI: GUI):
        Observer.__init__(self)
        self.model: (GA|None)=None
        self.ui: GUI =newGUI
        self.ui.attach(self)
        self.stop: bool=True

    def run(self):
        if self.ui==None or self.model==None:
            print("Program not set. Given parts: "+ str(self.ui) +str(self.model) )
        else:
            self.ui.appRun()

    def setModel(self, newModel: GA):
        self.model=newModel

    def setDefaultData(self):
        self.ui.data.algParams=[self.model.CROSS_CHANCE,self.model.MUT_CHANCE,self.model.POP_SIZE]
    def setLogSettings(self):
        print("set log params")
        self.model.logDest=self.ui.data.logDir

    def setParams(self):
        print("set alg params")
        self.ui.data.algParams = [x.value() for x in self.ui.paramSetWindow.paramValues]
        self.model.CROSS_CHANCE = self.ui.data.algParams[0]
        self.model.MUT_CHANCE = self.ui.data.algParams[1]
        self.model.POP_SIZE = round(self.ui.data.algParams[2])
        self.model.generatePopulation(self.model.POP_SIZE)
        self.model.TIME = round(self.ui.data.algParams[3])
        self.model.timeForRun=dt.timedelta(seconds=self.model.TIME)
        self.ui.refresh()

    def createLab(self):
        if self.ui.data.checkLab():
            self.model.labirynth.saveNewMatrix(self.ui.data.saveDir,self.ui.data.userLabirynth)
        else:
            self.ui.infoPopUp("Wrong labirynth format. Check size and used symbols.")
        print("create lab")

    def selectLabFromFile(self):
        if self.stop:
            print("selectLabFromFile")
            self.model.labirynth.loadMatrixFromFile(self.ui.data.getLabDir)
            self.ui.data.rawLabirynth=self.model.labirynth.__str__()
            self.ui.mainWindow.labirynthLabel.setText(self.ui.data.rawLabirynth)
        else:
            self.ui.infoPopUp("You cant change labirynth while algorithm is running")

    def stopAlg(self)->bool:
        if self.model.stopAfterTime():
            self.stop=True
        return self.stop

    def printLab(self):
        self.deltaOfUpdates: dt.timedelta = dt.timedelta(seconds=2)
        self.lastUpdate: datetime = datetime.now()
        while not self.stop:
            print("run")
            if(datetime.now()-self.lastUpdate)>=self.deltaOfUpdates:
                with self.model.lock:
                    self.lastUpdate = datetime.now()
                    if (self.model.bestInd != None):
                        self.ui.data.rawLabirynth=str(self.model.bestInd.labirynth)
                        self.ui.mainWindow.labirynthLabel.setText(self.ui.data.rawLabirynth)



    def startAlgorithm(self):
        self.stop=False
        lab=copy.deepcopy(self.model.labirynth)
        self.model=GA(lab,logDest=self.ui.data.logDir)
        self.setParams()
        self.algRun: threading.Thread=threading.Thread(target=self.model.run,args=(self.stopAlg,),daemon=True)
        self.algRun.start()

        self.labRefr: threading.Thread=threading.Thread(target=self.printLab, args=(), daemon=True)
        self.labRefr.start()



    def react(self, signal):

        match signal:
            case ActionType.getLab:
                self.selectLabFromFile()
            case ActionType.setLog:
                self.setLogSettings()
            case ActionType.run:
                if self.stop:
                    self.startAlgorithm()
                else:
                    self.ui.infoPopUp("The algorithm is already running.")
            case ActionType.setParam:
                self.setParams()
            case ActionType.stop:
                self.stop=True
            case ActionType.createLab:
                self.createLab()
