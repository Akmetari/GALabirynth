import Labirynth as l
import Individual as ind
import GA as ga

def testLabirynth():
    lab=l.Labirynth()
    print(lab.__str__()+"\n")  # Press Ctrl+F8 to toggle the breakpoint.
    return lab

def testIndividual(lab: l.Labirynth):
    eval=ga.GA(lab)
    i=ind.Individual(eval)
    print(i.__str__()+"\n")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test labiryntu: ")
    testIndividual(testLabirynth())

