from datetime import timedelta
from model.Labirynth import Labirynth
import model.Ind as ind
from Control import Controler
from GUI.GUI import GUI

from model.GA import GA



def testLabirynth()->Labirynth:
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
    #ctr=Controler(GUI())
    #ctr.setModel(GA(Labirynth()))

    #ctr.run()

    ga=GA(Labirynth(),popSize=1000)
    ga.logDest="D:\code\labirynthGA\GALabirynth\logs\mutation"
    ga.timeForRun=timedelta(seconds=600)


    ga.logDest = "D:\code\labirynthGA\GALabirynth\logs\popS"


    ga.POP_SIZE = 1000
    ga.run(ga.stopAfterIterations)

    ga.POP_SIZE = 100
    ga.run(ga.stopAfterIterations)






