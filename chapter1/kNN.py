from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1], [1.0,1.0], [0,0], [0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


#k top k item
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]                      #计算矩阵的行数
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet     #矩阵相减
    print(diffMat)
    sqDiffMat = diffMat**2                              #计算距离
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances**0.5                        #开平方，计算点与点之间的距离
    print(distances)
    sortedDistancesIndicies = distances.argsort()       #下标排序，数据的升序，然后取下标
    print(sortedDistancesIndicies)
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistancesIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


#将文件中的特征以及对应的分类解析为矩阵 matrix
def file2matrix(filename):
    fr = open(filename)
    numbersOfLines = len(fr.readline())
    returnMat = zeros((numbersOfLines, 3))
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index+=1
    return returnMat, classLabelVector


group, labels = createDataSet()

classify = classify0([1, 0], group, labels, 3)

print(classify)