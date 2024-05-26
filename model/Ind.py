import random

import model.Labirynth as l
import copy

MUTATION_SIZE=1

class Individual(object):

    def generateRandomPath(self):

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
    def getFitness(self)->float:
        if self.wasChanged:
            self.fitness=self.evaluator.evaluate(self)
        return self.fitness

    def __init__(self, evaluator, generate=True):
        self.labirynth=copy.deepcopy(evaluator.labirynth)
        self.fitness=100
        self.wasChanged=True
        self.evaluator=evaluator

        self.pathLen=random.randint(1, self.labirynth.xSize)

        if generate:
            self.generateRandomPath()


    def mutate(self):
        i=0
        while i<MUTATION_SIZE:
            i+=1
            x=random.randint(0,self.labirynth.xSize-1)
            y=random.randint(0,self.labirynth.ySize-1)

            if self.labirynth.matrix[x][y]!=9:
                if self.labirynth.matrix[x][y]==l.EMPTY:
                    self.pathLen+=1
                self.labirynth.matrix[x][y]=random.randint(0,4)

    def cross(self,partner):
        xStart=random.randint(0,self.labirynth.xSize-1)
        xEnd=random.randint(xStart,self.labirynth.xSize-1)
        yStart=random.randint(0,self.labirynth.ySize-1)
        yEnd=random.randint(yStart,self.labirynth.ySize-1)

        child1=Individual(self.evaluator,generate=False)
        child1.labirynth= copy.deepcopy(self.labirynth)
        child2=Individual(self.evaluator, generate=False)
        child2.labirynth = copy.deepcopy(partner.labirynth)

        for i in range(yStart,yEnd):
            for j in range (xStart, xEnd):
                if i in range(yStart,yEnd) and j in range(xStart, xEnd):
                    child2.labirynth.matrix[i][j]=self.labirynth.matrix[i][j]
                    child1.labirynth.matrix[i][j]=partner.labirynth.matrix[i][j]

        self.evaluator.removeFromPop(partner)
        self.evaluator.removeFromPop(self)

        self.evaluator.addToPop(child1)
        self.evaluator.addToPop(child2)

    def __str__(self):
        return ("Fitness: "+ str(self.getFitness()) +"\n"+ str(self.labirynth))

    def printInd(self):
        print("Path len= " +str(self.pathLen))
        print("Fitness= "+ str(self.getFitness()))
        self.labirynth.printLab()
        print("")






