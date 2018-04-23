from chapter6 import svmMliA

dataArr, labelArr = svmMliA.loadDataSet('testSet.txt')


b, alphas = svmMliA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)