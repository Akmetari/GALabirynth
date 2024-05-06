import Individual
from Labirynth import *
class GA(object):

    def __init__(self, labirynth:Labirynth, popSize=10 ):
        self.labirynth=labirynth
        self.population= self.generatePopulation(popSize,labirynth.xSize, labirynth.ySize)
        



    def generatePopulation(self, size, labRows, labCol):
        pop = []
        for i in range(size):
            pop.append(Individual(labRows, labCol, self))
        return pop