from chapter3 import trees
from chapter3 import treePlotter


lensesTree = trees.getLenseTree()

treePlotter.createPlot(lensesTree)

exit()
#获取数据
myData, labels = trees.createDataSet()

myTree = treePlotter.retrieveTree(0)
#print(myTree)

trees.storeTree(myTree, 'classifierStorage.txt')
print(trees.grabTree('classifierStorage.txt'))
#print(trees.classify(myTree, labels, [1, 1]))

#print(trees.chooseBestFeatureToSplit(myData))

#print(myData)
#myTree = trees.createTree(myData, labels)

#print(myTree)
#print(myData)
#print(trees.spliDataSet(myData, 0, 1))
#print(trees.spliDataSet(myData, 0, 0))
#print(myData[0][:2])
#myData[0][-1] = 'maybe'
#print(trees.calcShannonEnt(myData))

exit()

#treePlotter.createPlot()
#print(treePlotter.retrieveTree(0))
myTree0 = treePlotter.retrieveTree(0)
myTree1 = treePlotter.retrieveTree(1)
#print(treePlotter.getNumLeafs(myTree0))
#print(treePlotter.getTreeDepth(myTree0))
#print(treePlotter.getNumLeafs(myTree1))
print(myTree1)
myTree1['no surfacing'][2] = 'maybe'
print(myTree1)
treePlotter.createPlot(myTree1)