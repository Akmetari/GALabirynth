from GA import GA
from GUI import GUI

class Controler(object):

    def __init__(self):
        self.model: (GA|None)=None
        self.ui: (GUI|None)=None


    def run(self):
        if self.ui==None or self.mode==None:
            print("Program not set. Given parts: "+ str(self.ui) +str(self.model) )
        else:
            self.ui.appRun()

    def setGUI(self, newGUI):
        self.ui=newGUI

    def setModel(self, newModel):
        self.model=newModel