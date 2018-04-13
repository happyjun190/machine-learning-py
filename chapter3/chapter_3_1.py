from chapter3 import trees

#获取数据
myData, labels = trees.createDataSet()

#print(trees.chooseBestFeatureToSplit(myData))

#print(myData)
myTree = trees.createTree(myData, labels)

print(myTree)
#print(myData)
#print(trees.spliDataSet(myData, 0, 1))
#print(trees.spliDataSet(myData, 0, 0))
#print(myData[0][:2])
#myData[0][-1] = 'maybe'
#print(trees.calcShannonEnt(myData))