from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1], [1.0,1.0], [0,0], [0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


#k top k item
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]                      #计算矩阵的行数
    #print(dataSetSize)
    #print(dataSet)
    print(inX)
    #print(tile(inX, (dataSetSize, 1)))
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet     #矩阵相减
    sqDiffMat = diffMat**2                              #计算距离
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5                        #开平方，计算点与点之间的距离
    sortedDistancesIndicies = distances.argsort()       #下标排序
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistancesIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


#将文件中的特征以及对应的分类解析为矩阵 matrix
def file2matrix(filename):
    fr = open(filename)
    numbersOfLines = len(fr.readlines())
    returnMat = zeros((numbersOfLines, 3))
    classLabelVector = []
    fr = open(filename)
    index = 0
    #print(numbersOfLines)
    for line in fr.readlines():
        line = line.strip()
        #print(line)
        listFromLine = line.split('\t')
        #print(listFromLine)
        returnMat[index, :] = listFromLine[0:3]
        #classLabelVector.append(int(listFromLine[-1]))
        #classLabelVector.append(listFromLine[-1])
        if listFromLine[-1]=='didntLike':
            classLabelVector.append(1)
        elif listFromLine[-1]=='smallDoses':
            classLabelVector.append(2)
        elif listFromLine[-1]=='largeDoses':
            classLabelVector.append(3)
        else:
            classLabelVector.append(0)
        index+=1
    return returnMat, classLabelVector


#group, labels = createDataSet()

#classify = classify0([1, 0], group, labels, 3)

#@print(classify)

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    #print(maxVals)
    ranges = maxVals - minVals
    #print(ranges)
    #normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet/tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.10
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    #print(normMat)
    #print(ranges)
    #print(minVals)
    #exit()
    m = normMat.shape[0]
    numTestVecs = int(m*hoRatio)
    #print(numTestVecs)
    errorCount = 0
    for i in range(numTestVecs):
        #print(normMat[numTestVecs:m, :])
        #print(datingLabels[numTestVecs:m])
        classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %s, the real answer is: %s" % (classifierResult, datingLabels[i]))
        if(classifierResult != datingLabels[i]):errorCount+=1.0
    print("the total error rate is: %f " % (errorCount/float(numTestVecs)))
