"Data class is used to pass data form view to controler and the other way without messing with observer pattern. "


from model.GA import GA as ga

class Data():

    #labirynth display
    getLabDir:str="D:\code\labirynthGA\GALabirynth\labirynths\\"
    rawLabirynth:str=""

    #labirynth creation
    saveDir:str="D:\code\labirynthGA\GALabirynth\labirynths\\"
    xSize:int=1
    ySize:int=1
    legend: list[(str,str)]=[("Wall","9"),("Empty","0"),("Start","5"), ("End","8")]
    userLabirynth:str=""

    #log settings:
    logDir:str="D:\code\labirynthGA\GALabirynth\logs\\"
    logParams: list[bool]=[]

    #algorithm:
    algParams:list[float]=[ga.CROSS_CHANCE,ga.MUT_CHANCE,ga.POP_SIZE, ga.TIME]

    def __init__(self):
        print("")


    def checkLab(self)->bool: #checks if labirynth user inputed is correct due to its inputed size and characters allowed in labirynth definition
        labList= self.userLabirynth.split("\n")
        goodSize = len(labList)==self.ySize
        for row in labList:
            goodSize= goodSize and (len(row)==self.xSize)

        if not goodSize:
            return False

        signs=[]
        for t in self.legend:
            signs.append(t[1])

        for a in "".join(labList):
            if not a in signs:
                return False

        return True


