"""
Individual class represents single individual in genetic algorithms population. It contains labirynth with filled path of possible solution.
Path is represented by 4 directions that indicate in whitch way next step of path is being made.
"""

import random
import model.Labirynth as l
import copy

MUTATION_SIZE=1 #number of mutations in one individual

class Individual(object):

    def pickStart(self)->(int, int): #  (x,y)
        emptyCrates = []

        for i in range(self.labirynth.ySize):
            for j in range(self.labirynth.xSize):
                if self.labirynth.matrix[i][j] == l.EMPTY:
                    emptyCrates.append((j, i))


        return random.choice(emptyCrates)

    def generateRandomPath(self):

        #lastStep =self.startPoint#x,y
        lastStep=self.evaluator.labirynth.startPoint
        for i in range(self.pathLen):
            directionsToCheck=[1,2,3,4]

            while not (directionsToCheck==[]): #picking direction of next step untill it doesn't hit a wall or wont mean going back
                direction=random.choice(directionsToCheck)

                self.labirynth.matrix[lastStep[1]][lastStep[0]] = direction
                tmpStep=self.labirynth.makeStep(lastStep) #x,y
                if(tmpStep[0]>=0 and tmpStep[1]<self.labirynth.ySize and tmpStep[1]>=0 and tmpStep[0]<self.labirynth.xSize and self.labirynth.matrix[tmpStep[1]][tmpStep[0]] ==l.EMPTY):
                    lastStep = tmpStep
                    break
                else:
                    directionsToCheck.remove(direction) # delete thid direction from possible not to check them multiple times

            if (directionsToCheck==[]): # if there are no more moves to try its dead end so we stop path generation
                break
        self.findHole()

    def getFitness(self)->float:
        if self.wasChanged:
            self.fitness=self.evaluator.evaluate(self)
        return self.fitness

    def __init__(self, evaluator, generate=True):
        self.labirynth=copy.deepcopy(evaluator.labirynth)
        self.fitness=100
        self.wasChanged=True
        self.evaluator=evaluator
        self.startPoint=self.pickStart()
        self.firstHole=self.startPoint

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
        self.countLen()
        self.findHole()

    def patchworkMutate(self):
        if self.labirynth.matrix[self.firstHole[0]][self.firstHole[1]]!=9:
            self.labirynth.matrix[self.firstHole[0]][self.firstHole[1]] = random.randint(0, 4)
            self.countLen()
            self.findHole()

    def countLen(self):
        self.pathLen= sum(1 for row in self.labirynth.matrix for element in row if element != 0 and element != 9)
        if self.pathLen==0:
            print("dudu")
            self.labirynth.matrix[self.startPoint[1]][self.startPoint[0]]=1
            self.firstHole=self.startPoint
            self.pathLen=1

    def cross(self,partner):

        xStart=random.randint(0,self.labirynth.xSize-2)
        xEnd=random.randint(xStart,self.labirynth.xSize-1)
        yStart=random.randint(0,self.labirynth.ySize-2)
        yEnd=random.randint(yStart+1,self.labirynth.ySize-1)


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

        child1.countLen()
        child1.findHole()
        child2.countLen()
        child2.findHole()

        self.evaluator.addToPop(child1)
        self.evaluator.addToPop(child2)


    def findHole(self):
        position=self.startPoint
        for i in range(self.pathLen):
            next=self.labirynth.makeStep(position) #x,y

            if  next[0]>self.labirynth.xSize-1 or next[1]>self.labirynth.ySize-1 or next[0]<0 or next[1]<0:
                self.firstHole = (position[1], position[0])
                break
            elif self.labirynth.matrix[next[1]][next[0]]==9:
                self.firstHole = (position[1], position[0]) #yx
                break
            elif self.labirynth.matrix[next[1]][next[0]]==0:
                self.firstHole=(next[1],next[0]) # yx
                break
            position=next


    def __str__(self):
        return ("Fitness: "+ str(self.getFitness()) +"\n"+ str(self.labirynth))

    def printInd(self):
        print("Path len= " +str(self.pathLen))
        print("Fitness= "+ str(self.getFitness()))
        print("First hole= "+ str(self.firstHole))
        self.labirynth.printLab()
        print("")

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __gt__(self, other):
        return self.fitness < other.fitness






