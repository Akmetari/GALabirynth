from Individual import Individual
class GA(object):

    def __init__(self, labirynth, popSize=200 ):
        self.labirynth=labirynth
        self.population= self.generatePopulation(popSize)


    def generatePopulation(self, size):
        pop = []
        for i in range(size):
            pop.append(Individual(self))
        return pop