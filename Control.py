from GA import GA
from GUI import GUI

class Controler(object):

    def __init__(self):
        self.model: (GA|None)=None
        self.ui: (GUI|None)=None


    def run(self):
        if self.ui==None or self.model==None:
            print("Program not set. Given parts: "+ str(self.ui) +str(self.model) )
        else:
            self.ui.appRun()

    def setGUI(self, newGUI:GUI):
        self.ui=newGUI

    def setModel(self, newModel: GA):
        self.model=newModel

    def getLegend(self)->list[(str,str)]:
        return [()]

    def stop(self):
        print("stop")

    def browse(self):
        print("browse")

    def setLogSettings(self):
        print("set log settings")

    def setParams(self):
        print("set alg params")

    def createLab(self):
        print("create lab")

    def startCreateLab(self):
        print("start create lab")