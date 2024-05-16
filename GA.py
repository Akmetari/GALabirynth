import time

from Individual import Individual
import random
MUT_CHANCE=100
CROSS_CHANCE=50


class GA(object):

    def __init__(self, labirynth, popSize=20, logDest="D:\code\labirynthGA\GALabirynth" ):
        self.labirynth=labirynth
        self.population= self.generatePopulation(popSize)
        self.logDest=logDest
        self.fileName="log.txt"


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


    def setLogDest(self,dest):
        self.logDest=dest
    def log(self, fileName=""):

        # stworzyć plik jeśli nie istnieje AAAAAAAAAAAAAAAAAAAAAA
        if fileName=="":
            fileName=self.fileName

        with open(self.logDest+fileName,"w") as file:
            file.write(self.generateLog())

    def generateLog(self):
        return "Log"

    def run(self, stopPred):
        self.fileName="labirynthGenAlg"+ str(time.time())+".txt"

        while not stopPred():
            self.cross()
            self.mutate()
            self.log(fileName=self.fileName)


    def printGA(self):
        print("Labirynth: ")
        self.labirynth.printLab()
        print("\n Population:")
        for i in self.population:
            i.printInd()