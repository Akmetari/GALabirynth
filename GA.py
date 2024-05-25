import threading
from datetime import datetime
from datetime import timedelta
from Ind import Individual
import random



class GA(object):
    MUT_CHANCE = 0.1
    CROSS_CHANCE = 60
    TIME= 3600 #time is seconds
    POP_SIZE=100
    def __init__(self, labirynth, popSize=20, logDest="D:\code\labirynthGA\GALabirynth", runTime=timedelta(seconds=TIME)  ):
        self.labirynth=labirynth
        self.population= self.generatePopulation(popSize)
        self.logDest=logDest
        self.fileName="log.txt"
        self.bestInd:Individual=None
        self.bestFit=100
        self.diversityLevel=0
        self.lock = threading.Lock()

        self.startTime=datetime.now()
        self.timeForRun=runTime
    def generatePopulation(self, size):
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
    def mutate(self):
        for ind in self.population:
            if(random.uniform(0.0,100.0))<self.MUT_CHANCE:
                ind.mutate()

    def evaluate(self,ind : Individual)->float: # calculates fitness of individual, we will minimize the function
        pathCheck= ind.labirynth.pathCheck(ind)
        pathWalked= pathCheck[1] if pathCheck[1]>0 else 1
        continous= 0.4 if pathCheck[0] else 2
        solution= 0.2 if ind.labirynth.isSolution(ind) else 1
        startEnd= 0.5 if ind.labirynth.isStartAndEnd(ind) else 1

        fitness= 10*(1/pathWalked) *continous*solution*startEnd # może uwzględniać pitagorejską odległość końca ścieżki od wyjścia labiryntu

        return fitness

    def removeFromPop(self,ind):
        self.population.remove(ind)

    def addToPop(self,ind):
        self.population.append(ind)
    def countDiversity(self)->float:
        #porównanie fitness, wybranie losowych punktów i sprawdzenie, w ilu miejscach sie różnią?
        return 0
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
        self.startTime = datetime.now()
        self.fileName="labirynthGenAlg"+ str(self.startTime.timestamp())+".txt"
        self.population=self.generatePopulation(self.POP_SIZE)
        self.findBest()



        while not stopPred():
            self.cross()
            self.mutate()
            self.findBest()
         #   self.bestInd.printInd()
            #self.log(fileName=self.fileName)

    def findBest(self):
        bestFit=self.population[0].getFitness()
        bestInd=self.population[0]

        for ind in self.population:
            newFit=ind.getFitness()
            if newFit<bestFit:
                bestFit= newFit
                bestInd=ind

        with self.lock:
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