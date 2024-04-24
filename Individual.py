import random


class Individual(object):
    def __init__(self, rows, columns, evaluator):
        self.path=[]
        self.fitness=0
        self.wasChanged=false
        self.evaluator=evaluator

        for i in range(rows):
            row=[]
            for j in rage(columns):
                row.append(0)
            self.path.append(row)
        generateRandomPath(self,randint(len(self.path)-1))


    def generateRandomPath(self, pathLen):
        for i in range(pathLen):
            randSquare=randint(len(self.path)-1)
            self.path[randSquare]=1

    def getFitness(self):
        if self.wasChanged:
            fitness=self.evaluator.evaluate(self)
        return self.fitness



