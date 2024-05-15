from Individual import Individual
import random
MUT_CHANCE=0.001
CROSS_CHANCE=50


class GA(object):

    def __init__(self, labirynth, popSize=200 ):
        self.labirynth=labirynth
        self.population= self.generatePopulation(popSize)


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

    def log(self):
        print("log")
    def run(self, stopPred):

        while not stopPred():
            self.cross()
            self.mutate()