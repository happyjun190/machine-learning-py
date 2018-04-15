from math import log
import operator

#香农熵计算
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0   #用于初始化数据，如果没有key就初始化为0
        labelCounts[currentLabel] += 1      #用户增量数据，每次加1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        #print(prob)
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


#创建数据集
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']
               ]

    labels = ['no surfacing', 'flippers']
    return dataSet, labels


#分割数据集
def spliDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


#选择最佳的特征
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeatures = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = spliDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob*calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        #print("index: %d, baseEntropy:%f, newEntropy:%f" % (i, baseEntropy, newEntropy))

        if infoGain>bestInfoGain:
            bestInfoGain = infoGain
            bestFeatures = i
    return bestFeatures

# 选举
def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


#构建决策树
def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    #print("classList.count(classList[0]):%d, len(classList):%d" % (classList.count(classList[0]), len(classList)))
    #print(classList[0])
    #print(classList.count(classList[0]) == len(classList))
    #print(len(dataSet[0]))
    if classList.count(classList[0]) == len(classList):
        #print(classList[0])
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    #print(bestFeatLabel)
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(spliDataSet(dataSet, bestFeat, value), subLabels)
    return myTree

#分类器
def classify(inputTree, featLabels, testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


#存储决策树-持久化决策树
def storeTree(inputTree, fileName):
    import pickle
    fw = open(fileName, 'wb')
    #inputTree = str(inputTree)
    #print(inputTree)
    #inputTree = str(inputTree)
    pickle.dump(inputTree, fw)
    fw.close()

#获取决策树句柄
def grabTree(fileName):
    import pickle
    fr = open(fileName, 'rb')
    return pickle.load(fr)


#获取眼科病决策树
def getLenseTree():
    fr = open('lenses.txt')
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lenseLabels = ['age', 'prescript', 'astigmatic', 'tearRate']
    lenseTree = createTree(lenses, lenseLabels)
    #print(lenseTree)
    return lenseTree