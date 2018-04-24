from chapter6 import svmMliA
from numpy import *

dataArr, labelArr = svmMliA.loadDataSet('testSet.txt')


b, alphas = svmMliA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)

print('b=====================> %s' % b)
#print('alphas================> %s' % alphas)
print('alphas================> %s' % alphas[alphas>0])

print(shape(alphas[alphas>0]))

for i in range(100):
    if alphas[i] > 0:
        print("dataArr[%d] : %s, labelArr[%d]: %s " % (i,dataArr[i], i, labelArr[i]))