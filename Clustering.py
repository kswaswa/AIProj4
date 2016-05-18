#Katie Swanson
#proj 4

import sys
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import scipy.interpolate as interp

X = []
Y = []
numClusters = 0
clusterX = []
clusterY = []
centers = []

def main():
    global numClusters
    if (len(sys.argv) != 3):
        print('Need 4 args\n')
        exit(1)
    filename = sys.argv[2]
    numClusters = sys.argv[1]
    numClusters = int(numClusters)
    readInFile(filename)
    initClusters(numClusters)
    updatePoints()
    plotPoints()

def readInFile(filename):
    global X
    global Y
    f = open(filename, 'r')
    for line in f:
        x, y = line.split()
        x = float(x)
        y = float(y)
        X.append(x)
        Y.append(y)
    f.close()

def initClusters(numClusters):
    global X, Y, clusterX, clusterY, centers
    for j in range(numClusters):
        i = random.randint(0, len(X)-1)
        x = X[i]
        y = Y[i]
        clusterX.append([x])
        clusterY.append([y])
        centers.append([[[x, y]]])

def updateClusters(centersJ, minX, minY):
    global clusterX, clusterY, centers
    sumX = 0
    sumY = 0
    for i in centers[centersJ]:
        sumX += i[0][0]
        sumY += i[0][1]

    aveX = sumX / len(centers[centersJ])
    aveY = sumY / len(centers[centersJ])
    #update the X and Y cluster center lists with new ave X and Y for matching Z/cluster
    centers[centersJ].append([[minX, minY]])
    clusterX[centersJ] = [aveX]
    clusterY[centersJ] = [aveY]

def myDistance(xCenter, yCenter, xCoord, yCoord):
    return math.sqrt((xCoord - xCenter)**2 + (yCoord - yCenter)**2)

def updatePoints():
    global X, Y, clusterX, clusterY, centers

    for i in range(len(X)):
        xCoord = X[i]
        yCoord = Y[i]
        min = 100000000000000
        minJ = 100000000000000
        minX = 100000000000000
        minY = 100000000000000
        for j in range(len(centers)):
            myDist = myDistance(clusterX[j][0], clusterY[j][0], xCoord, yCoord) 
            if (myDist < min):
                min = myDist
                minJ = j
                minX = xCoord
                minY = yCoord
        updateClusters(minJ, minX, minY)

def plotPoints():
    global clusterX, clusterY, centers
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']
    for i in range(len(centers)):
        for j in range(len(centers[i])):
            ax.scatter(centers[i][j][0][0], centers[i][j][0][1], c=colors[i])
    plt.show()

main()
