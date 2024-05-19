from datetime import timedelta

from Labirynth import Labirynth
import Ind as ind

from GA import GA

def testLabirynth():
    lab=Labirynth()
    lab.printLab() # Press Ctrl+F8 to toggle the breakpoint.
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
    ga.timeForRun=timedelta(minutes=1)
    ga.run(ga.stopAfterTime)
def testCross(ga):
    ga.printGA()
    ga.cross()
    ga.printGA()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test labiryntu: ")
    testMainLoop(GA(Labirynth(),popSize=50))

