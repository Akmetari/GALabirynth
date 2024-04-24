import Individual
class GA(object):

    def __init__(self, labirynth, popSize ):
        self.labirynth=labirynth
        self.population= self.generatePopulation(popSize,len(labirynth), len(labirynth[0]))
        



    def generatePopulation(self, size, labRows, labCol):
        pop = []
        for i in range(size):
            pop.append(Individual(labRows, labCol, self))
        return pop