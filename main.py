from Labirynth import Labirynth
import Individual as ind
import random
from datetime import datetime
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test labiryntu: ")
    random.seed(datetime.now().timestamp())
    testPopulation(GA(testLabirynth(),popSize=5))

