import random
import Labirynth as l

class Individual(object):

    def generateRandomPath(self, pathLen):

        if random.randint(0,100)%2==0:
            lastStep=self.evaluator.labirynth.startPoint
        else:
            lastStep = self.evaluator.labirynth.endPoint

        for i in range(pathLen):
            nextWall=True
            directionsChecked=[0,0,0,0]
            possibleMove=True

            while nextWall and possibleMove: #picking direction of next step untill it doesn't hit a wall or wont mean going back
                direction=random.randint(4)

                match direction: #checking if there is no wall in next step
                    case l.RIGHT:
                       if (self.labirynth.matrix[lastStep[0]+1][lastStep[1]] == l.WALL) or (not self.labirynth.matrix[lastStep[0]+1][lastStep[1]] ==l.EMPTY): #prawo
                           directionsChecked[0]=1
                           nextWall=True
                       else:
                           nextWall=False
                           self.labirynth.matrix[lastStep[0]][lastStep[1]] = l.RIGHT
                           lastStep = (lastStep[0] + 1, lastStep[1])
                    case l.UP:
                        if (self.labirynth.matrix[lastStep[0]][lastStep[1]+1] == l.WALL) or (not self.labirynth.matrix[lastStep[0]+1][lastStep[1]] ==l.EMPTY) : #góra
                            directionsChecked[1] = 2
                            nextWall = True
                        else:
                            nextWall = False
                            self.labirynth.matrix[lastStep[0]][lastStep[1]] = l.UP
                            lastStep = (lastStep[0], lastStep[1] + 1)
                    case l.LEFT:
                        if (self.labirynth.matrix[lastStep[0] -1][lastStep[1]] == l.WALL) or (not self.labirynth.matrix[lastStep[0]+1][lastStep[1]] ==l.EMPTY) :#lewo
                            directionsChecked[2] = 3
                            nextWall = True
                        else:
                            nextWall = False
                            self.labirynth.matrix[lastStep[0]][lastStep[1]] = l.LEFT
                            lastStep = (lastStep[0] - 1, lastStep[1])
                    case l.DOWN:
                        if (self.labirynth.matrix[lastStep[0]][lastStep[1]-1] == l.WALL) or (not self.labirynth.matrix[lastStep[0]+1][lastStep[1]] ==l.EMPTY): #dół
                            directionsChecked[3] = 4
                            nextWall = True
                        else:
                            nextWall = False
                            self.labirynth.matrix[lastStep[0]][lastStep[1]] = l.DOWN
                            lastStep = (lastStep[0], lastStep[1] - 1)

                if not (0 in directionsChecked):
                    possibleMove=False
            if not possibleMove:
                break


    def getFitness(self):
        if self.wasChanged:
            fitness=self.evaluator.evaluate(self)
        return self.fitness
    def __init__(self, rows, columns, evaluator):
        self.labirynth=evaluator.labirynth
        self.fitness=0
        self.wasChanged=False
        self.evaluator=evaluator

        self.generateRandomPath(self, random.randint(len(self.labirynth.xSize)/2))


    def __str__(self):
        return ("Fitness: "+self.fitness +"\n"+ self.labirynth.__str__())






