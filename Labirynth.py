
WALL=9
EMPTY=0
RIGHT=1
LEFT=3
UP=2
DOWN=4
DEF_X_SIZE=20
DEF_Y_SIZE=20
DEF_START=(0,1)
DEF_END=(DEF_X_SIZE,DEF_Y_SIZE)


class Labirynth(object):
    def __init__(self, x=DEF_X_SIZE, y=DEF_Y_SIZE, startPt=DEF_START, endPt=DEF_END):
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


    def __str__(self):
        str=""

        for x in self.matrix:
            for y in self.matrix[x]:
                str=str+ self.matrix[x][y]+"  "
            str+="\n"

        return str


    def fillLabirynth(self,walls):  # wals in form of tuples representing squares of labirynth eg. (1,3)
        for w in walls:
            self.matrix[w[0]][w[1]]=WALL #fills matrix with wall symbol where assigned by walls

    def passes(self, path):
        passes=True;

        return passes


