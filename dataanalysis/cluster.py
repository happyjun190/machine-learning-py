from numpy import genfromtxt, zeros

data = genfromtxt('iris.csv', delimiter=',', usecols=(0,1,2,3))
target = genfromtxt('iris.csv', delimiter=',', usecols=(4), dtype=str)

t = zeros(len(target))
t[target == 'setosa'] = 1
t[target == 'versicolor'] = 2
t[target == 'virginica'] = 3

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
#classifier.fit(data, t)# training on the iris dataset
#print(classifier.predict(data[0]))


from sklearn.model_selection import train_test_split
train, test, t_train, t_test = train_test_split(data, t, test_size=0.4, random_state=0)

classifier.fit(train, t_train)

#print(classifier.score(test, t_test))

from sklearn.metrics import confusion_matrix
#print(confusion_matrix(classifier.predict(test), t_test))

from sklearn.metrics import classification_report
#print(classification_report(classifier.predict(test), t_test, target_names=['setosa', 'versicolor', 'virginica']))

from sklearn.model_selection import cross_val_score
#scores = cross_val_score(classifier, data, t, cv=6)
#print(scores)

#from numpy import mean
#print(mean(scores))

from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=3, init='random')# initialization
kmeans.fit(data)# actual execution

c = kmeans.predict(data)

from sklearn.metrics import completeness_score, homogeneity_score
print(completeness_score(t, c))
print(homogeneity_score(t, c))

from pylab import subplot, plot, show, figure
figure()
subplot(211) # top figure with the real classes
plot(data[t==1,0],data[t==1,2],'bo')
plot(data[t==2,0],data[t==2,2],'ro')
plot(data[t==3,0],data[t==3,2],'go')
subplot(212) # bottom figure with classes assigned automatically
show()
