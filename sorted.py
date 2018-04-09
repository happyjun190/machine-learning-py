from operator import itemgetter

l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(l))
print(sorted(l, reverse=True))
print(sorted(l, key=lambda t:t[0]))
print(sorted(l, key=lambda t:t[1], reverse=True))

print(sorted(l, key=itemgetter(0)))