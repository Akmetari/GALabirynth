from Labirynth import Labirynth
import Individual as ind
from GA import GA

def testLabirynth():
    lab=Labirynth()
    print(str(lab)+"\n")  # Press Ctrl+F8 to toggle the breakpoint.
    return lab

def testIndividual(labirynth):
    eval=GA(labirynth)
    i=ind.Individual(eval)
    print(str(i)+"\n")

def testPopulation(ga):
    for ind in ga.population:
        print(str(ind))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test labiryntu: ")
    testPopulation(GA(testLabirynth(),10))

