"""
Main model class, instance of genetic algorithm optimizator. Runs main optimization loop and contains both population
and plain labirynth classes. Evaluates Individual instances and manages logging generations.

Uses basic stop function based on working time.
"""
import copy
import threading
from datetime import datetime
from datetime import timedelta
from typing import Callable

from model.Ind import Individual
from model.Labirynth import Labirynth
import model.Labirynth as lab
import random


class GA(object):
    MUT_CHANCE = 0.1
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
        self.worstFit:float=100
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
    def cutBranch(self,original: Individual,branchStart):

        ind= Individual(self,False)
        ind.labirynth=copy.deepcopy(original.labirynth)
        now=branchStart
        nextStep=ind.labirynth.makeStep(now)

        while nextStep!=now:
            tmp=ind.labirynth.makeStep(nextStep)
            ind.labirynth.matrix[nextStep[1]][nextStep[0]]=0

            now=nextStep
            nextStep=tmp

        return ind
    def cutIndBranches(self, ind:Individual):

        propositions=[]
        fitneses=[]

        for cross in self.labirynth.crossroads:
            ifBranch=ind.labirynth.checkIfBranch(cross)
            if ifBranch[0]:
                for path in ifBranch[1]:
                    propositions.append(self.cutBranch(ind,path))

                for i in propositions:
                    fitneses.append(i.getFitness())

                bestNum= fitneses.index(min(fitneses))
                self.addToPop(propositions[bestNum])
                self.removeFromPop(ind)

    def removeBranches(self):
        for p in self.population:
            self.cutIndBranches(p)



    def rankingCross(self):
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
                ind.patchworkMutate()
    def evaluate(self,ind : Individual)->float: # calculates fitness of individual, we will minimize the function
        pathCheck= ind.labirynth.pathCheck(ind)
        pathWalked= pathCheck[1] if pathCheck[1]>0 else self.labirynth.xSize*self.labirynth.ySize
        continous= 0.4 if pathCheck[0] else 10
        solution= 0.2 if ind.labirynth.isSolution(ind) else 1
        startEnd= 0.5 if ind.labirynth.isStartAndEnd(ind) else 2

        fitness= (10/ind.pathLen)  # może uwzględniać pitagorejską odległość końca ścieżki od wyjścia labiryntu

        return fitness

    def removeFromPop(self,ind: Individual):
        if ind in self.population:
            self.population.remove(ind)

    def addToPop(self,ind: Individual):
        self.population.append(ind)

    def setLogDest(self,dest: str):
        self.logDest=dest
    def log(self,i: int, fileName: str=""):
        filePath:str=self.logDest+fileName
        with open(filePath,"a") as file:
            file.write(self.generateLog(i)+"\n")

    def generateLog(self, i:int)->str:
        return ""+str(i)+" popS: "+str(self.POP_SIZE)+ " mut: "+ str(self.MUT_CHANCE)+ " cros: "+ str(self.CROSS_CHANCE)+ " "+"Bfit: "+str(self.bestFit)+ " "+"Wfit: "+ str(self.worstFit)

    def run(self, stopPred: Callable):
        self.startTime = datetime.now()
        self.fileName="labirynthGenAlg"+ str(self.startTime.timestamp())+".txt"
        self.population=self.generatePopulation(self.POP_SIZE)
        self.findBest()
        i=0
        while not stopPred(i,600):
            self.rankingCross()
            #self.removeBranches()
            self.mutate()
            self.findBest()
            if i%10==0:
                self.bestInd.printInd()
            self.log(i,fileName=self.fileName)
            i+=1

    def findBest(self):
        bestFit=self.population[0].getFitness()
        bestInd=self.population[0]
        worstFit=bestFit

        for ind in self.population:
            newFit=ind.getFitness()
            if newFit<bestFit:
                bestFit= newFit
                bestInd=ind
            if newFit>worstFit:
                worstFit=newFit

        with self.lock:
            self.bestInd=bestInd
            self.bestFit=bestFit
            self.worstFit=worstFit

    def printGA(self):
        print("Labirynth: ")
        self.labirynth.printLab()
        print("\n Population:")
        for i in self.population:
            i.printInd()

    def stopAfterTime(self):
        return (datetime.now()-self.startTime >=self.timeForRun)

    def stopAfterIterations(self, itNumber, maxIt):
        return itNumber>=maxIt