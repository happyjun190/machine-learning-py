from chapter7 import adaboost
from numpy import *

dataMat, classLabels = adaboost.loadSimpData()

D = mat(ones((5,1))/5)

bestStump, minError, bestClasEst = adaboost.buildStump(dataMat, classLabels, D)

print(bestStump)
print(minError)
print(bestClasEst)

