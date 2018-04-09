from numpy import *

#生成一个4*4的矩阵
randMat = mat(random.rand(4,4))
print(randMat)
#获取到矩阵的逆
invRandMat = randMat.I

print(invRandMat)

print(invRandMat*randMat)

print(eye(4))
#print(type(randMat))