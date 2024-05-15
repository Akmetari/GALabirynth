import random
import Labirynth as l

class Individual(object):  

    def generateRandomPath(self, pathLen):

        lastStep=self.evaluator.labirynth.startPoint
       # self.labirynth.matrix[lastStep[1]][lastStep[0] ]=5

        for i in range(pathLen):
            directionsToCheck=[1,2,3,4]

            while not (directionsToCheck==[]): #picking direction of next step untill it doesn't hit a wall or wont mean going back
                direction=random.choice(directionsToCheck)

                match direction: #checking if there is no wall in next step
                    case l.RIGHT:
                       if (lastStep[0]+1>=self.labirynth.xSize) or (self.labirynth.matrix[lastStep[1]][lastStep[0]+1] !=l.EMPTY): #prawo
                           directionsToCheck.remove(1)

                       else:
                           self.labirynth.matrix[lastStep[1]][lastStep[0]] = l.RIGHT
                           lastStep = (lastStep[0] + 1,lastStep[1])
                           break
                    case l.UP:
                        if ((lastStep[1]-1<0) or
                                ( self.labirynth.matrix[lastStep[1]-1][lastStep[0]] !=l.EMPTY)) : #góra
                            directionsToCheck.remove(2)

                        else:
                            self.labirynth.matrix[lastStep[0]][lastStep[1]] = l.UP
                            lastStep = ( lastStep[0],lastStep[1]-1)
                            break
                    case l.LEFT:
                        if (lastStep[0]-1<0) or (self.labirynth.matrix[lastStep[1]][lastStep[0]-1] !=l.EMPTY) :#lewo
                            directionsToCheck.remove(3)

                        else:
                            self.labirynth.matrix[lastStep[1]][lastStep[0]] = l.LEFT
                            lastStep = ( lastStep[0]- 1,lastStep[1])
                            break
                    case l.DOWN:
                        if ((lastStep[1]+1>self.labirynth.ySize) or
                                (self.labirynth.matrix[lastStep[1]+1][lastStep[0]] !=l.EMPTY)): #dół
                            directionsToCheck.remove(4)

                        else:
                            self.labirynth.matrix[lastStep[1]][lastStep[0]] = l.DOWN
                            lastStep = ( lastStep[0],lastStep[1]+ 1 )
                            break
            if (directionsToCheck==[]):
                break


    def getFitness(self):
        if self.wasChanged:
            fitness=self.evaluator.evaluate(self)
        return self.fitness
    def __init__(self, evaluator):
        self.labirynth=evaluator.labirynth
        self.fitness=0
        self.wasChanged=False
        self.evaluator=evaluator

        self.generateRandomPath(random.randint(1, round(self.labirynth.xSize/2)))


    def __str__(self):
        return ("Fitness: "+ str(self.fitness) +"\n"+ str(self.labirynth))






