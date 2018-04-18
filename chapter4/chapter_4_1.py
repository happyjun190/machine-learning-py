from chapter4 import bayes
import re
import feedparser

ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')

ny['entries']
print(len(ny['entries']))
exit()

#针对标点符号进行正则匹配
#regEx = re.compile('\\W*')
#mySent = "This book is the best book on Python or M.L. I have ever laid eyes upon."

#listOfTokens = regEx.split(mySent)
#print(listOfTokens)

#listOfTokens = [word.lower() for word in listOfTokens if len(word) > 0]
#print(listOfTokens)
E
#emailText = open('email/ham/6.txt').read()
#listOfTokens = regEx.split(emailText)
#listOfTokens = [word.lower() for word in listOfTokens if len(word) > 0]
#print(listOfTokens)

bayes.spamTest()

exit()


bayes.testingNB()

exit()
listOPosts, listClasses = bayes.loadDataSet()

myVocabList = bayes.createVocableList(listOPosts)
print(myVocabList)


trainMat = []

for postinDoc in listOPosts:
    #print(postinDoc)
    trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))


p0V, p1V, pAb = bayes.trainNB0(trainMat, listClasses)

print(pAb)
print(p0V)
print(p1V)

#print(trainMat)