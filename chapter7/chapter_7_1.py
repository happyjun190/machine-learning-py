from chapter7 import adaboost
from numpy import *

dataArr, labelArr = adaboost.loadDataSet('horseColicTraining2.txt')

classifierArray,aggClassEst = adaboost.adaBoostTrainDS(dataArr,labelArr,10)

adaboost.plotROC(aggClassEst.T,labelArr)
exit()


dataArr, labelArr = adaboost.loadDataSet('horseColicTraining2.txt')
classifierArray = adaboost.adaBoostTrainDS(dataArr, labelArr, 10)

testArr,testLabelArr = adaboost.loadDataSet('horseColicTest2.txt')
prediction10 = adaboost.adaClassify(testArr,classifierArray)

errArr=mat(ones((67,1)))
print(errArr[prediction10!=mat(testLabelArr).T].sum())


exit()
dataMat, classLabels = adaboost.loadSimpData()

classifierArray = adaboost.adaBoostTrainDS(dataMat, classLabels, 9)

#print(classifierArray)

exit()

D = mat(ones((5,1))/5)

bestStump, minError, bestClasEst = adaboost.buildStump(dataMat, classLabels, D)

print(bestStump)
print(minError)
print(bestClasEst)

