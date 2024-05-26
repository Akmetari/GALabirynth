import copy
import datetime as dt
from datetime import datetime
import threading
from model.GA import GA
from GUI.GUI import GUI
from GUI.GUI import ActionType
from model.Labirynth import Labirynth
from observer import  Observer

class Controler(Observer):

    def __init__(self, newGUI: GUI):
        Observer.__init__(self)
        self.model: (GA|None)=None
        self.ui: GUI =newGUI
        self.ui.attach(self)
        self.stop: bool=False

    def run(self):
        if self.ui==None or self.model==None:
            print("Program not set. Given parts: "+ str(self.ui) +str(self.model) )
        else:
            self.ui.appRun()

    def setModel(self, newModel: GA):
        self.model=newModel

    def setDefaultData(self):
        self.ui.data.algParams=[self.model.CROSS_CHANCE,self.model.MUT_CHANCE,self.model.popSize]
    def setLogSettings(self):
        print("set log params")

    def setParams(self):
        print("set alg params")
        self.ui.data.algParams = [x.value() for x in self.ui.paramSetWindow.paramValues]
        self.model.CROSS_CHANCE = self.ui.data.algParams[0]
        self.model.MUT_CHANCE = self.ui.data.algParams[1]
        self.model.POP_SIZE = int(self.ui.data.algParams[2])
        self.model.generatePopulation(self.model.POP_SIZE)
        self.model.TIME = int(self.ui.data.algParams[3])

        self.ui.refresh()

    def createLab(self):
        if self.ui.data.checkLab():
            self.model.labirynth.saveNewMatrix(self.ui.data.saveDir,self.ui.data.userLabirynth)
        else:
            self.ui.showPopUp("Wrong labirynth format. Check size and used symbols.")
        print("create lab")

    def selectLabFromFile(self):
        print("selectLabFromFile")
        self.model.labirynth.loadMatrixFromFile(self.ui.data.getLabDir)
        self.ui.data.rawLabirynth=self.model.labirynth.__str__()
        self.ui.mainWindow.labirynthLabel.setText(self.ui.data.rawLabirynth)


    def stopAlg(self)->bool:
        return self.model.stopAfterTime() or self.stop

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
        self.model=GA(lab)
        self.setParams()
        self.model.timeForRun = dt.timedelta(minutes=1)
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
                self.startAlgorithm()
            case ActionType.setParam:
                self.setParams()
            case ActionType.stop:
                self.stop=True
            case ActionType.createLab:
                self.createLab()
