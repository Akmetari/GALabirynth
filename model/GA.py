"""
Main model class, instance of genetic algorithm optimizator. Runs main optimization loop and contains both population
and plain labirynth classes. Evaluates Individual instances and manages logging generations.

Uses basic stop function based on working time.
"""

import threading
from datetime import datetime
from datetime import timedelta
from typing import Callable

from model.Ind import Individual
from model.Labirynth import Labirynth
import random
class GA(object):
    MUT_CHANCE = 60
    CROSS_CHANCE = 60
    TIME= 3600 #time in seconds
    POP_SIZE=100
    def __init__(self, labirynth: Labirynth, popSize: int=POP_SIZE, logDest:str="D:\code\labirynthGA\GALabirynth\\", runTime: timedelta=timedelta(seconds=TIME)  ):
        self.labirynth: Labirynth=labirynth
        self.POP_SIZE=popSize
        self.population :list[Individual]= self.generatePopulation(popSize)
        self.logDest: str=logDest
        self.fileName: str="logText.txt"
        self.bestInd:(Individual|None)=None
        self.bestFit: float=100
        self.diversityLevel: float=0
        self.lock: threading.Lock = threading.Lock()

        self.startTime: datetime=datetime.now()
        self.timeForRun: timedelta=runTime
    def generatePopulation(self, size: int):
        pop = []
        for i in range(size):
            pop.append(Individual(self))
        return pop

    def cross(self):
        for ind in self.population:
            if(random.uniform(0.0,100.0))<self.CROSS_CHANCE:
                partner=random.choice(self.population)
                while partner==ind:
                    partner= random.choice(self.population)

                ind.cross(partner)

    def tournamentCross(self):
        sortedPop: list[Individual]= sorted(self.population)

        for i in range(0,int(self.POP_SIZE/2)):
            sortedPop[i].cross(sortedPop[self.POP_SIZE -1 - i])
            if i<3:
                self.removeFromPop(sortedPop[self.POP_SIZE - 1 - i])
                self.removeFromPop(sortedPop[self.POP_SIZE - 1])  # deleting worst to maintain same pop size
            else:
                self.removeFromPop(sortedPop[i])
                self.removeFromPop(sortedPop[self.POP_SIZE - 1 - i])

    def mutate(self):
        for ind in self.population:
            if(random.uniform(0.0,100.0))<self.MUT_CHANCE:
                #ind.patchworkMutate()
                ind.patchworkMutate()
    def evaluate(self,ind : Individual)->float: # calculates fitness of individual, we will minimize the function
        pathCheck= ind.labirynth.pathCheck(ind)
        pathWalked= pathCheck[1] if pathCheck[1]>0 else 1
        continous= 0.4 if pathCheck[0] else 2
        solution= 0.2 if ind.labirynth.isSolution(ind) else 1
        startEnd= 0.5 if ind.labirynth.isStartAndEnd(ind) else 1

        fitness= 10*(1/pathWalked) *continous*solution*startEnd # może uwzględniać pitagorejską odległość końca ścieżki od wyjścia labiryntu

        return fitness

    def removeFromPop(self,ind: Individual):
        if ind in self.population:
            self.population.remove(ind)

    def addToPop(self,ind: Individual):
        self.population.append(ind)
    def countDiversity(self)->float:
        #porównanie fitness, wybranie losowych punktów i sprawdzenie, w ilu miejscach sie różnią?
        return 0
    def setLogDest(self,dest: str):
        self.logDest=dest
    def log(self, fileName: str=""):
        filePath:str=self.logDest+fileName
        with open(filePath,"a") as file:
            file.write(self.generateLog()+"\n")

    def generateLog(self)->str:
        return ""+str(datetime.now().timestamp())+" popS: "+str(self.POP_SIZE)+" fit: "+str(self.bestFit)+" div: "+str(self.countDiversity())

    def run(self, stopPred: Callable):
        self.startTime = datetime.now()
        self.fileName="labirynthGenAlg"+ str(self.startTime.timestamp())+".txt"
        self.population=self.generatePopulation(self.POP_SIZE)
        self.findBest()
        self.printGA()
        i=0
        while not stopPred():
            self.tournamentCross()
            self.mutate()
            self.findBest()
            print(str(i)+ " hole: " + str(self.bestInd.firstHole))
            if i%10==0:
                self.bestInd.printInd()
            self.log(fileName=self.fileName)
            i+=1

    def findBest(self):
        bestFit=self.population[0].getFitness()
        bestInd=self.population[0]

        for ind in self.population:
            newFit=ind.getFitness()
            if newFit<bestFit:
                bestFit= newFit
                bestInd=ind

        #with self.lock:
        self.bestInd=bestInd
        self.bestFit=bestFit

    def printGA(self):
        print("Labirynth: ")
        self.labirynth.printLab()
        print("\n Population:")
        for i in self.population:
            i.printInd()

    def stopAfterTime(self):
        return (datetime.now()-self.startTime >=self.timeForRun)