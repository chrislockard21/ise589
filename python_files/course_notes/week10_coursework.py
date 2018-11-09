import math
import matplotlib.pyplot as plt
from random import uniform, seed
# Global var
numRich = 250
numPoor = 250
numNeighbors = 15
reqnumType = 3


class Agent():
    def __init__(self, type):
        self.type = type
        self.randLoc()

    def randLoc(self):
        self.location = (uniform(0,1), uniform(0,1))

    def updateLoc(self, agent):
        while not self.ishappy(agents):
            self.randLoc()

    def getDistance(self, neighbor):
        # Euclidean distance
        x = (self.location[0] - neighbor.location[0])**2
        y = (self.location[1] - neighbor.location[1])**2
        return math.sqrt(x+y)

    def ishappy(self, agents):
        distances = []
        for agent in agents:
            if self != agent:
                distance = self.getDistance(agent)
                distances.append((distance, agent))
        distances.sort()

        neighbors = [agent for d,agent in distances[:numNeighbors]]
        numSameType = sum([self.type == agent.type for agent in neighbors])

        return numSameType >= reqnumType

def plotagents(agents):
    xVal_R, yVal_R = [], []
    xVal_P, yVal_P = [], []

    for agent in agents:
        x,y = agent.location
        if agent.type == 0:
            xVal_R.append(x)
            yVal_R.append(y)
        elif agent.type == 1:
            xVal_P.append(x)
            yVal_P.append(y)

    fig, ax = plt.subplots(figsize=(6,6))
    ax.plot(xVal_R, yVal_R, 'o', markerfacecolor='green', markersize=6)
    ax.plot(xVal_P, yVal_P, 'o', markerfacecolor='red', markersize=6)
    ax.set_title('Cycle Count {}'.format(count))
    plt.show()
#-------------------------------------------------------------------------------
agents = [Agent(0) for i in range(numRich)]
agents.extend([Agent(1) for i in range(numPoor)])
count = 1
while True:
    noMove = True
    plotagents(agents)
    count += 1
    for agent in agents:
        oldLoc = agent.location
        agent.updateLoc(agents)
        if oldLoc != agent.location:
            noMove = False
    if noMove:
        break
