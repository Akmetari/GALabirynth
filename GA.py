from datetime import datetime
from datetime import timedelta

from Individual import Individual
import random
MUT_CHANCE=100
CROSS_CHANCE=50


class GA(object):

    def __init__(self, labirynth, popSize=20, logDest="D:\code\labirynthGA\GALabirynth", runTime=timedelta(hours=1)  ):
        self.labirynth=labirynth
        self.population= self.generatePopulation(popSize)
        self.logDest=logDest
        self.fileName="log.txt"
        self.bestInd=None
        self.bestFit=100

        self.startTime=datetime.now()
        self.timeForRun=runTime


    def generatePopulation(self, size):
        pop = []
        for i in range(size):
            pop.append(Individual(self))
        return pop

    def cross(self):
        print("crossover")
    def mutate(self):
        for ind in self.population:
            if(random.uniform(0.0,100.0))<MUT_CHANCE:
                ind.mutate()


    def evaluate(self,ind : Individual)->float: # calculates fitness of individual, we will minimize the function
        pathCheck= ind.labirynth.pathCheck(ind)
        pathWalked= pathCheck[1] if pathCheck[1]>0 else 1
        continous= 0.4 if pathCheck[0] else 2
        solution= 0.2 if ind.labirynth.isSolution(ind) else 1
        startEnd= 0.5 if ind.labirynth.isStartAndEnd(ind) else 1

        fitness= (1/pathWalked) *continous*solution*startEnd *(1/ind.pathLen)

        return fitness
    def setLogDest(self,dest):
        self.logDest=dest
    def log(self, fileName=""):

        # stworzyć plik jeśli nie istnieje AAAAAAAAAAAAAAAAAAAAAA
        if fileName=="":
            fileName=self.fileName

        with open(self.logDest+fileName,"w") as file:
            file.write(self.generateLog())

    def generateLog(self)->str:
        return "Log"

    def run(self, stopPred):
        self.fileName="labirynthGenAlg"+ str(datetime.now().timestamp())+".txt"

        while not stopPred():
            self.cross()
            self.mutate()
            self.findBest()
            self.log(fileName=self.fileName)


    def findBest(self):
        bestFit=self.population[0].getFitness()
        bestInd=self.population[0]

        for ind in self.population:
            newFit=ind.getFitness()
            if newFit<bestFit:
                bestFit= newFit
                bestInd=ind

        self.bestInd=bestInd
        self.bestFit=bestFit

    def printGA(self):
        print("Labirynth: ")
        self.labirynth.printLab()
        print("\n Population:")
        for i in self.population:
            i.printInd()

    def stopAfterTime(self):
        return (self.startTime-datetime.now() >=self.timeForRun)