from GA import GA
from GUI import GUI
from observer import  Observer

class Controler(Observer):

    def __init__(self, newGUI: GUI):
        Observer.__init__(self)
        self.model: (GA|None)=None
        self.ui: GUI =newGUI
        self.ui.attach(self)


    def run(self):
        if self.ui==None or self.model==None:
            print("Program not set. Given parts: "+ str(self.ui) +str(self.model) )
        else:
            self.ui.appRun()

    def setModel(self, newModel: GA):
        self.model=newModel

    def stop(self):
        print("stop")

    def setLogSettings(self):
        print("set log settings")

    def setParams(self):
        print("set alg params")

    def createLab(self):
        print("create lab")

    def startCreateLab(self):
        print("start create lab")

    def selectLabFromFile(self):
        print("selectLabFromFile")

    def react(self, signal):
        print("reaction: " + str(signal))