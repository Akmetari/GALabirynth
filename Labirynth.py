
WALL=9
EMPTY=0
RIGHT=1
LEFT=3
UP=2
DOWN=4
DEF_X_SIZE=11
DEF_Y_SIZE=11
DEF_START=(0,1)
DEF_END=(DEF_X_SIZE-1,DEF_Y_SIZE-1)
DEF_WALLS=[(0,0),(1,0),(5,0),
           (2,1),(3,1),(4,1),(5,1),(6,1),(8,1),(9,1),
           (0,2),(2,2),(6,2),(10,2),
           (0,3),(4,3),(6,3),(7,3),(8,3),(10,3),
           (1,4),(2,4),(4,4),(10,4),
           (2,5),(4,5),(6,5),(7,5),(8,5),(10,5),
           (0,6),(1,6),(2,6),(7,6),(10,6),
           (4,7),(5,7),(7,7),(9,7),(10,7),
           (0,8),(1,8),(3,8),(7,8),(9,8),
           (1,9),(3,9),(5,9),(6,9),(8,9),(9,9),
           (3,10)]



class Labirynth(object):

    def __init__(self, x=DEF_X_SIZE, y=DEF_Y_SIZE, startPt=DEF_START, endPt=DEF_END, walls=DEF_WALLS):
        self.xSize=x
        self.ySize=y
        self.startPoint=startPt
        self.endPoint=endPt

        self.matrix= []

        for i in range(x): #creating empty matrix
            row=[]
            for j in range(y):
                row.append(EMPTY)
            self.matrix.append(row)
        self.fillLabirynth(walls)


    def __str__(self):
        s=""

        for row in self.matrix:
            r=""
            for a in row:
                r=r+str(a)+" "
            s+=r+"\n"
        return s


    def printLab(self):
        for row in self.matrix:
            for a in row:
                if a>0 and a<5:
                    print("\033[34m"+str(a)+" ", end="")
                elif a==9:
                    print("\033[31m" + str(a) + " ", end="")
                else:
                    print("\033[37m"+str(a) + " ", end="")
            print("")

    def fillLabirynth(self,walls):  # wals in form of tuples representing squares of labirynth eg. (1,3)
        for w in walls:
            self.matrix[w[1]][w[0]]=WALL #fills matrix with wall symbol where assigned by walls


    def passes(self, individual):
        position=self.startPoint

        for i in range(individual.pathLen):
            next=self.makeStep(position)
            if self.matrix[next[1]][next[0]] ==EMPTY: # if there is empty tile in path it means it isnt continuous
                return False

        if position==self.endPoint: # if after whole pass position is exit of labirynth, it has been passed
            return True
        else:
            return False

    def makeStep(self, position:()): #returns position after step coded on given labirynth crate
        direction=self.matrix[position[1]][position[0]]

        if direction == RIGHT:
            return (position[0]+1,position[1])
        elif direction == UP:
            return (position[0], position[1]-1)
        elif direction == LEFT:
            return (position[0]-1,position[1])
        elif direction == DOWN:
            return (position[0], position[1]+1)
        else:
            return position
