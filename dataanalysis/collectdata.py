from urllib import request

url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = request.urlopen(url)
localFile = open('iris.csv', 'wb+')
localFile.write(u.read())
localFile.close()