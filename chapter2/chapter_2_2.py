from numpy.core.multiarray import array

from chapter2 import kNN
import matplotlib
import matplotlib.pyplot as plt

#datingTestSet.txt 分别为 飞行英里数/year、玩游戏时间/%，冰激凌消耗量/周，类型
#1、Number of frequent flyer miles earned per year
#2、Percentage of time spent playing video games
#3、Liters of ice cream consumed per week
#4、classify

imgVector = kNN.handwritingClassTest()
#print(imgVector)
exit()
kNN.classifyPerson()
exit()

kNN.datingClassTest()
exit()

datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')

#print(datingDataMat)

#print(datingLabels[0:20])
normDataSet, ranges, minVals = kNN.autoNorm(datingDataMat)



print(normDataSet)
print(ranges)
print(minVals)
exit()

fig = plt.figure()
ax = fig.add_subplot(111)


#print(datingDataMat[0][0])
#print(datingDataMat[:,0][0])
#print(datingDataMat[0][0]==datingDataMat[:,0][0])

#print(len(datingDataMat[:,1]))
#print(array(datingLabels))
#print(15*datingLabels)
print(type(datingLabels))
ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15*array(datingLabels), 15*array(datingLabels))
plt.show()