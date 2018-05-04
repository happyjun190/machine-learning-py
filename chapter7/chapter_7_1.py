from chapter7 import adaboost
from numpy import *

dataMat, classLabels = adaboost.loadSimpData()

classifierArray = adaboost.adaBoostTrainDS(dataMat, classLabels, 9)

#print(classifierArray)

exit()

D = mat(ones((5,1))/5)

bestStump, minError, bestClasEst = adaboost.buildStump(dataMat, classLabels, D)

print(bestStump)
print(minError)
print(bestClasEst)

