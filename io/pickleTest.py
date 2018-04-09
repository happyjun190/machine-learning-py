import pickle
d = dict(name="Bob", age=20, score=80)
print(pickle.dumps(d))

f = open('pickle.txt', 'wb')
pickle.dump(d, f)
f.close()

f = open('pickle.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)