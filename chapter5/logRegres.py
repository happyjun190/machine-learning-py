from math import *
from numpy import *

#载入数据集
def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('testSet.txt')
    for line in fr.readlines():
        lineArr = list(line.strip().split())
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat

#定义函数: 1/(1+e-z)
def sigmoid(inX):
    return 1.0 / (1 + exp(-inX))

#梯度上升算法
def gradAscend(dataMatIn, classLabels):
    dataMatrix = mat(dataMatIn)                                     #m*n矩阵
    labelMat = mat(classLabels).transpose()                         #转置 1*m 矩阵
    m, n = shape(dataMatrix)                                        #获取行列数
    alpha = 0.001                                                   #步值 step
    maxCycles = 500                                                 #迭代次数
    weights = ones((n, 1))                                          #n*1矩阵
    for k in range(maxCycles):
        h = sigmoid(dataMatrix * weights)                           #m*n * n*1 = m*1
        error = (labelMat - h)                                      #m*1-m*1 = m*1
        weights = weights + alpha * dataMatrix.transpose() * error  #C * (m*n)T * m*1 = C * (n*m * m*1) = C * n*1
    return weights


#Plotting the logistic regression best-fit line and dataset
def plotBestFit(wei):
    import matplotlib.pyplot as plt
    weights = wei.getA()
    dataMat, labelMat = loadDataSet()
    dataArr = array(dataMat)
    n = shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1]); ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1]); ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')

    x = arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2')
    plt.show()


#Stochastic gradient ascent
def stocGradAscend0(dataMatrix, classLabels):
    m, n = shape(dataMatrix)
    alpha = 0.01
    weightsTmp = ones(n)
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i] * weightsTmp))
        error = classLabels[i] - h
        weightsTmp = weightsTmp + alpha * error * dataMatrix[i]

    #返回为矩阵格式
    weights = zeros((n, 1))
    for i in range(n):
        weights[i][0] = weightsTmp[i]

    return weights

#Modified stochastic gradient ascent
def stocGradAscend1(dataMatrix, classLabels, numIter=150):
    m, n = shape(dataMatrix)
    weightsTmp = ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.01
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMatrix[randIndex]*weightsTmp))
            error = classLabels[randIndex]-h
            weightsTmp = weightsTmp + alpha*error*dataMatrix[randIndex]
            del(dataIndex[randIndex])

    # 返回为矩阵格式
    weights = zeros((n, 1))
    for i in range(n):
        weights[i][0] = weightsTmp[i]

    return weights
