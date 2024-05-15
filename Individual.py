import random
import Labirynth as l
import copy

class Individual(object):  

    def generateRandomPath(self):

        tmp=0
        lastStep=self.evaluator.labirynth.startPoint
        for i in range(self.pathLen):
            directionsToCheck=[1,2,3,4]

            while not (directionsToCheck==[]): #picking direction of next step untill it doesn't hit a wall or wont mean going back
                direction=random.choice(directionsToCheck)

                self.labirynth.matrix[lastStep[1]][lastStep[0]] = direction
                tmpStep=self.labirynth.makeStep(lastStep)
                if(tmpStep[0]>0 and tmpStep[0]<self.labirynth.ySize and tmpStep[1]>0 and tmpStep[1]<self.labirynth.xSize and self.labirynth.matrix[tmpStep[1]][tmpStep[0]] ==l.EMPTY):
                    lastStep = tmpStep
                    break
                else:
                    directionsToCheck.remove(direction) # delete thid direction from possible not to check them multiple times
                    self.labirynth.matrix[lastStep[1]][lastStep[0]] = l.EMPTY

            if (directionsToCheck==[]): # if there are no more moves to try its dead end so we stop path generation
                break
    def getFitness(self):
        if self.wasChanged:
            fitness=self.evaluator.evaluate(self)
        return self.fitness
    def __init__(self, evaluator):
        self.labirynth=copy.deepcopy(evaluator.labirynth)
        self.fitness=0
        self.wasChanged=False
        self.evaluator=evaluator

        self.pathLen=random.randint(4, self.labirynth.xSize)
        self.generateRandomPath()


    def __str__(self):
        return ("Fitness: "+ str(self.fitness) +"\n"+ str(self.labirynth))






