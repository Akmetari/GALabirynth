"""
Labirynth class contains matrix representing labirynth grid. It contains methods checking Individual by its path
and methods to save and load labirynth from file.
"""


import json

WALL=9
EMPTY=0
START=5
END=8
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

    def __init__(self, x:int=DEF_X_SIZE, y:int=DEF_Y_SIZE, startPt:(int,int)=DEF_START, endPt: (int, int)=DEF_END, walls:list[(int,int)]=DEF_WALLS):
        self.xSize: int=x
        self.ySize: int=y
        self.startPoint: (int, int)=startPt
        self.endPoint: (int, int)=endPt

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

    def stringToMatrix(self,string:str)->list:
        newMatrix=[]
        splitStr=string.split("\n")
        for line in splitStr:
            newMatrix.append([int(a) for a in list(line)])
        return newMatrix

    def checkMatrix(self,matrix):
        return self.checkMatrixLen(matrix) and self.checkOnlyAcceptableSigns(matrix)
    def checkMatrixLen(self,matrix: list[list[int]])->bool:
        equalLen=True
        firstRowLen=len(matrix[0])
        for row in matrix:
            equalLen=equalLen and len(row)==firstRowLen

        return equalLen

    def checkOnlyAcceptableSigns(self,matrix: list[list[int]]):
        goodSigns=True
        for row in matrix:
            for a in row:
                goodSigns=goodSigns and (a==EMPTY or a==WALL or a==START or a==END)
                if not goodSigns:
                    return False

        return goodSigns

    def saveNewMatrix(self,filePath:str,string:str): #file path should be generated based on user preference or in designed location
        newMatrix= self.stringToMatrix(string)
        if self.checkMatrix(newMatrix):
            with open(filePath, "w") as file:
                json.dump(newMatrix,file)
        else:
            print("This array has wrong format.")
            #popup error


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

    def fillLabirynth(self,walls: list[(int,int)]):  # walls in form of tuples representing squares of labirynth eg. (1,3)
        for w in walls:
            self.matrix[w[1]][w[0]]=WALL #fills matrix with wall symbol where assigned by walls

    def loadMatrixFromFile(self,filePath:str):
        with open(filePath, "r") as file:
            self.matrix=json.load(file)

        y=0
        for row in self.matrix:
            x=0
            for el in row:
                if el==START:
                    self.startPoint=(x,y)
                elif el==END:
                    self.endPoint = (x, y)
                x += 1
            y += 1

        self.xSize=len(self.matrix[0])
        self.ySize=len(self.matrix)




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

    def makeStep(self, position:(int,int))->(int,int): #returns position after step coded on given labirynth crate
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
