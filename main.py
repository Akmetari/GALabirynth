from datetime import timedelta
from Labirynth import Labirynth
import Ind as ind
from Control import Controler
from GUI import GUI

from GA import GA



def testLabirynth():
    lab=Labirynth()
    lab.printLab()
    return lab

def testIndividual(labirynth):
    eval=GA(labirynth)
    i=ind.Individual(eval)
    i.printInd()

def testPopulation(ga):
    for ind in ga.population:
        ind.printInd()

def testMutation(ga):
    ga.mutate()

def testMainLoop(ga):
    ga.timeForRun=timedelta(minutes=30)
    ga.run(ga.stopAfterTime)
def testCross(ga):
    ga.printGA()
    ga.cross()
    ga.printGA()

def testMatrixSave():
    lab=Labirynth()
    strMatrix= "99500900000\n00999990990\n90900890009"
    lab.saveNewMatrix("D:\code\labirynthGA\GALabirynth\matrix.txt",strMatrix)

def testMatrixLoad():
    lab=Labirynth()
    lab.loadMatrixFromFile("D:\code\labirynthGA\GALabirynth\matrix.txt")
    lab.printLab()
    print("x: "+str(lab.xSize))
    print("y: "+str(lab.ySize))

if __name__ == '__main__':
    ctr=Controler(GUI.GUI())
    ctr.setModel(GA(Labirynth()))

    ctr.run()

