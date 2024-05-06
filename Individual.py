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
                       if (self.path[lastStep[0]+1][lastStep[1]] == l.WALL) or (not self.path[lastStep[0]+1][lastStep[1]] ==l.EMPTY): #prawo
                           directionsChecked[0]=1
                           nextWall=True
                       else:
                           nextWall=False
                    case l.UP:
                        if (self.path[lastStep[0]][lastStep[1]+1] == l.WALL) or (not self.path[lastStep[0]+1][lastStep[1]] ==l.EMPTY) : #góra
                            directionsChecked[1] = 2
                            nextWall = True
                        else:
                            nextWall = False
                    case l.LEFT:
                        if (self.path[lastStep[0] -1][lastStep[1]] == l.WALL) or (not self.path[lastStep[0]+1][lastStep[1]] ==l.EMPTY) :#lewo
                            directionsChecked[2] = 3
                            nextWall = True
                        else:
                            nextWall = False
                    case l.DOWN:
                        if (self.path[lastStep[0]][lastStep[1]-1] == l.WALL) or (not self.path[lastStep[0]+1][lastStep[1]] ==l.EMPTY): #dół
                            directionsChecked[3] = 4
                            nextWall = True
                        else:
                            nextWall = False

                if not (0 in directionsChecked):
                    possibleMove=False

            if possibleMove:
                match direction:
                    case l.RIGHT:
                        self.path[lastStep[0]][lastStep[1]] = l.RIGHT
                        lastStep=(lastStep[0]+1,lastStep[1])
                    case l.UP:
                        self.path[lastStep[0]][lastStep[1]] = l.UP
                        lastStep = (lastStep[0], lastStep[1]+1)
                    case l.LEFT:
                        self.path[lastStep[0]][lastStep[1]] = l.LEFT
                        lastStep = (lastStep[0] - 1, lastStep[1])
                    case l.DOWN:
                        self.path[lastStep[0]][lastStep[1]] = l.DOWN
                        lastStep = (lastStep[0] , lastStep[1]-1)
            else:
                break


    def getFitness(self):
        if self.wasChanged:
            fitness=self.evaluator.evaluate(self)
        return self.fitness
    def __init__(self, rows, columns, evaluator):
        self.path=[]
        self.fitness=0
        self.wasChanged=False
        self.evaluator=evaluator

        for i in range(rows):
            row=[]
            for j in range(columns):
                row.append(0)
            self.path.append(row)
        self.generateRandomPath(self, random.randint(len(self.path) - 1))


    def __str__(self):



        return






