# python tester.py FILENAME EPSILON TRAIN% THR
# python tester.py input.csv 0.1 20 -90
import sys
import csv
import random

class Model:
    def __init__(self, arms):
        self.successes = [0] * arms
        self.uses = [0] * arms

# looks at current exploration and returns current best arm 
    def getProbability(self, arm):
        try:
            return (self.successes[arm])/(self.uses[arm]) 
        except ZeroDivisionError:                               # arm hasn't been tried yet
            return 0

    def getBestArm(self):
        maxProb = 0
        arm = -1
        for i in range(0, len(self.successes)):
            try:
                if maxProb < (self.successes[i])/(self.uses[i]):
                    maxProb = (self.successes[i])/(self.uses[i])
                    arm = i
            except ZeroDivisionError:
                continue
        if arm == -1:                                                           # all arms have not had any success/usage
            return random.randrange(0, len(self.successes))
        else:
            return arm

    def trainModel(self, data, epsilon, thr):
        for row in range(0, len(data)):
            p = random.uniform(0, 1)
            if p<epsilon:                                                       # explore
                arm = random.randrange(0, len(self.successes))
                self.uses[arm] += 1
                if float(data[row][arm])<thr:
                    self.successes[arm] += 1
            else:                                                               # exploit
                arm = self.getBestArm()
                self.uses[arm] += 1
                if float(data[row][arm])<thr:
                    self.successes[arm] += 1     

    def testModel(self, data, arm, thr):
        successes = 0
        for row in range(0, len(data)):
            if float(data[row][arm])<thr:
                successes += 1
        return successes/len(data)

if (len(sys.argv) != 5):
    print("ERROR: Not enough or too many input arguments.")
    exit()
filename = sys.argv[1]
try:
    epsilon = float(sys.argv[2])
    if epsilon<0 or epsilon>1:
        epsilon = 0.3
    train = int(sys.argv[3])
    if train<0 or train>50:
        train = 50
except ValueError:
    epsilon = 0.3
    train = 50
try:
    thr = float(sys.argv[4])
except ValueError:
    print("Invalid Threshold Value")
    exit()
print("epsilon: " + str(epsilon))
print("Training data percentage: " + str(train) + "%")
print("Success threshold: " + str(thr) + "\n")

try:
    with open(filename, mode ='r')as file:
        csvFile = csv.reader(file)
        file = []
        for lines in csvFile:
            file.append(lines)
except FileNotFoundError:
    print("ERROR: Not enough/too many/illegal input arguments.")
    exit()
trainingSize = int(((train/100)*(len(file)-1))//1)
trainingSet = []
testSet = []
for i in range(1, trainingSize+1):
    trainingSet.append(file[i])
for i in range(trainingSize+1, len(file)):
    testSet.append(file[i])
currentModel = Model(len(file[0]))
currentModel.trainModel(trainingSet, epsilon, thr)

print("Success probabilities:")
for i in range(0, len(file[0])):
    print("P(" + str(file[0][i]) + ") = " + str(currentModel.getProbability(i)))
bestBandit = currentModel.getBestArm() + 1
print("\nBandit [" + str(bestBandit) + "] was chosen to be played for the rest of data set.")
# print(str(bestBandit) + " Success percentage: " + str(currentModel.getProbability(bestBandit - 1)))
testResults = currentModel.testModel(testSet, bestBandit-1, thr)
print(str(bestBandit) + " Success percentage: " + str(testResults))



# for i in range(0, len(currentModel.successes)):
#     print(currentModel.uses[i])