from GA import GA as ga

class Data():

    #labirynth display
    getLabDir:str="D:/code/"
    rawLabirynth:str=""
    formatedLabirynth:str=""

    #labirynth creation
    saveDir:str=""
    xSize:int=1
    ySize:int=1
    legend: list[(str,str)]=[("Wall","9"),("Empty","0"), ("Right","1"),("Left","3"), ("Up","2"), ("Down","4"), ("Start","5"), ("End","8")]
    userLabirynth:str=""

    #log settings:
    logDir:str=""
    logParams: list[bool]=[]

    #algorithm:
    algParams:list[float]=[ga.CROSS_CHANCE,ga.MUT_CHANCE,ga.POP_SIZE, ga.TIME]

    def __init__(self):
        print("")


    def checkLab(self)->bool:
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


