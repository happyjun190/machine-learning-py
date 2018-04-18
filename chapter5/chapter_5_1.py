from chapter5 import logRegres
from numpy import *

logRegres.multiTest()

exit()

dataArr, labelMat = logRegres.loadDataSet()

#weights = logRegres.gradAscend(dataArr, labelMat)
weights = logRegres.stocGradAscend1(array(dataArr), labelMat, 500)

logRegres.plotBestFit(mat(weights))