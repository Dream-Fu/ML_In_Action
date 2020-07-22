from numpy import *


def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = list(map(float, curLine))
        dataMat.append(fltLine)
    fr.close()
    return dataMat


def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:, j])
        rangeJ = float(max(dataSet[:, j] - minJ))
        centroids[:, j] = minJ + rangeJ * random.rand(k, 1)
    return centroids


def kMeans(dataSet, k, distMeans=distEclud, createCent=randCent):
    m = shape(dataSet)[0]
    clusterAssement = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                distJI = distMeans(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssement[i, 0] != minIndex: clusterChanged = True
            clusterAssement[i, :] = minIndex, minDist ** 2
        print(centroids)
        for cent in range(k):
            ptsInClust = dataSet[nonzero(clusterAssement[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInClust, axis=0)
    return centroids, clusterAssement



datMat = mat(loadDataSet(r'testSet.txt'))
# print(datMat)
# print(min(datMat[:, 0]))
# print(min(datMat[:, 1]))
# print(max(datMat[:, 0]))
# print(max(datMat[:, 1]))
# print(randCent(datMat, 2))
# print(datMat[0])
# print(distEclud(datMat[0], datMat[1]))
myCentroids, clustAssing = kMeans(datMat, 4)
