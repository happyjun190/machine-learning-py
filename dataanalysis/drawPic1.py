from pylab import plot, show
from numpy import genfromtxt

data = genfromtxt('iris.csv', delimiter=',', usecols=(0,1,2,3))
target = genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)

#print(set(target))

plot(data[target=='setosa', 0], data[target=='setosa', 2], 'bo')
plot(data[target=='versicolor', 0], data[target=='versicolor', 2], 'ro')
plot(data[target=='virginica', 0], data[target=='virginica', 2], 'go')
show()