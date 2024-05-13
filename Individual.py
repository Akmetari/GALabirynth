import random
import Labirynth as l

class Individual(object):  #brak ograniczen generowania kroków Eby poza mape nie wychodzilo

    def generateRandomPath(self, pathLen):

        lastStep=self.evaluator.labirynth.startPoint
        self.labirynth.matrix[lastStep[1]][lastStep[0] ]=5

        for i in range(pathLen):
            directionsChecked=[0,0,0,0]
            possibleMove=True

            while 0 in directionsChecked: #picking direction of next step untill it doesn't hit a wall or wont mean going back
                direction=random.randint(0,4)

                match direction: #checking if there is no wall in next step
                    case l.RIGHT:
                       if (self.labirynth.matrix[lastStep[1]][lastStep[0]+1] == l.WALL) or (not self.labirynth.matrix[lastStep[1]][lastStep[0]+1] ==l.EMPTY): #prawo
                           directionsChecked[0]=1

                       else:
                           self.labirynth.matrix[lastStep[1]][lastStep[0]] = l.RIGHT
                           lastStep = (lastStep[1], lastStep[0] + 1)
                    case l.UP:
                        if (self.labirynth.matrix[lastStep[1]-1][lastStep[0]] == l.WALL) or (not self.labirynth.matrix[lastStep[1]-1][lastStep[0]] ==l.EMPTY) : #góra
                            directionsChecked[1] = 2

                        else:

                            self.labirynth.matrix[lastStep[0]][lastStep[1]] = l.UP
                            lastStep = (lastStep[1]-1, lastStep[0])
                    case l.LEFT:
                        if (self.labirynth.matrix[lastStep[1] ][lastStep[0]-1] == l.WALL) or (not self.labirynth.matrix[lastStep[1]][lastStep[0]-1] ==l.EMPTY) :#lewo
                            directionsChecked[2] = 3

                        else:

                            self.labirynth.matrix[lastStep[1]][lastStep[0]] = l.LEFT
                            lastStep = (lastStep[1] , lastStep[0]- 1)
                    case l.DOWN:
                        if (self.labirynth.matrix[lastStep[1]+1][lastStep[0]] == l.WALL) or (not self.labirynth.matrix[lastStep[1]+1][lastStep[0]] ==l.EMPTY): #dół
                            directionsChecked[3] = 4

                        else:

                            self.labirynth.matrix[lastStep[1]][lastStep[0]] = l.DOWN
                            lastStep = (lastStep[1]+ 1, lastStep[0] )

            if not possibleMove:
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






