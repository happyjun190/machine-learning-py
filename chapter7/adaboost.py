from numpy import *

def loadSimpData():
    datMat = matrix([[1. , 2.1],
                     [2. , 1.1],
                     [1.3, 1. ],
                     [1. , 1. ],
                     [2. , 1. ]
                     ])
    classLables = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat, classLables

#Listing 7.1 Decision stump–generating functions
def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    retArray = ones((shape(dataMatrix)[0], 1))
    if threshIneq == 'lt':
        #print('threshIneq: %s, dataMatrix[:, dimen]: %s. threshVal: %s' % (threshIneq, dataMatrix[:, dimen], threshVal))
        retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
    else:
        #print('threshIneq: %s, dataMatrix[:, dimen]: %s. threshVal: %s' % (threshIneq, dataMatrix[:, dimen], threshVal))
        retArray[dataMatrix[:, dimen] > threshVal] = -1.0
    #print("retArray: %s" % retArray)
    return retArray

def buildStump(dataArr, classLabels, D):
    dataMatrix = mat(dataArr); labelMat = mat(classLabels).T
    m, n = shape(dataMatrix)
    numSteps = 10.0; bestStump = {}; bestClasEst = mat(zeros((m, 1)))
    minError = inf
    for i in range(n):
        rangeMin = dataMatrix[:, i].min(); rangeMax = dataMatrix[:, i].max()

        stepSize = (rangeMax - rangeMin) / numSteps
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']:
                threshVal = (rangeMin + float(j) * stepSize)
                #print(threshVal)
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)
                errArr = mat(ones((m, 1)))

                #print(predictedVals == labelMat)

                errArr[predictedVals == labelMat] = 0
                #print(errArr)
                weightedError = D.T * errArr

                #print("split: dim %d, thresh %.2f, thresh ineqal:  %s, the weighted error is %.3f" % (i, threshVal, inequal, weightedError))

                if weightedError < minError:
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClasEst

#Listing 7.2 AdaBoost training with decision stumps
def adaBoostTrainDS(dataArr, classLabels, numIt=40):
    weakClassArr = []
    m = shape(dataArr)[0]
    D = mat(ones((m, 1)) / m)
    aggClassEst = mat(zeros((m, 1)))
    for i in range(numIt):
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)
        print('D: %s' % D.T)
        alpha = float(0.5 * log((1 - error)/ max(error, 1e-16)))
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        print('classEst: %s' % classEst.T)
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
        D = multiply(D, exp(expon))
        D = D / D.sum()
        aggClassEst += alpha * classEst
        print('aggClassEst: %s' % classEst.T)
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggErrors.sum() / m
        print('total error: %f' % errorRate)
        if errorRate == 0.0: break
    return weakClassArr

#Listing 7.3 AdaBoost classification function
def adaClassify(datToClass, classifierArr):
    dataMatrix = mat(datToClass)
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m, 1)))
    for i in range(len(classifierArr)):
        classEst = stumpClassify(dataMatrix, classifierArr[i]['dim'], classifierArr[i]['thresh'], classifierArr[i]['ineq'])
        aggClassEst += classifierArr[i]['alpha'] * classEst
    return sign(aggClassEst)


#Listing 7.4 Adaptive load data function
def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t'))
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        lineArr = [float(curLine[i]) for i in range(numFeat - 1)]
        dataMat.append(lineArr)
        labelMat.append(float(curLine[-1]))
    return dataMat, labelMat
