
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
            print("\033[37m"+"")

    def fillLabirynth(self,walls):  # walls in form of tuples representing squares of labirynth eg. (1,3)
        for w in walls:
            self.matrix[w[1]][w[0]]=WALL #fills matrix with wall symbol where assigned by walls


    def pathCheck(self, individual)-> (bool,int): #checks if path is continuous and doesn't hit any wall, returns info if bad step and length of path walked before it
        position=self.startPoint
        steps=0
        for i in range(individual.pathLen):
            next=self.makeStep(position)
            steps+=1
            if self.matrix[next[1]][next[0]] ==EMPTY or self.matrix[next[1]][next[0]] ==WALL : # if there is empty tile/ wall in path it means it isnt continuous/ wont get us anywhere
                return (False,steps)

        return (True,steps)

    def isSolution(self, individual)->bool:
        return self.pathCheck(individual)[0] and self.isStartAndEnd(individual)

    def isStartAndEnd(self,individual)->bool:
        return individual.labirynth.matrix[self.startPoint[1]][self.startPoint[0]] != EMPTY and individual.labirynth.matrix[self.endPoint[1]][self.endPoint[0]] != EMPTY

    def makeStep(self, position:())->(int,int): #returns position after step coded on given labirynth crate
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
