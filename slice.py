#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Iterable
i = 1;
l = []
while i < 101:
    l.append(i)
    i = i + 1
    #print(l)

#print(l[::5])
#print(l[-10:])

l1 = list(range(101))
#print(l1)
print(l1[:10:2])

d = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'ac': 3}

for key in d:
    print(key, ":",d[key])

for values in d.values():
    print(values)

for key, values in d.items():
    print(key,":",values)

noit = "aaa"

print(isinstance(d, Iterable))
print(isinstance(noit, Iterable))

def findMinAndMax(list=[0,1]):
    max = 0
    min = 0
    for i in list:
        if max < i:
            max = i
        if min > i:
            min = i
    return (max, min)

print(l1)
print(findMinAndMax(l1))

print([x*x for x in range(9+1)])


L = ['Hello', 'World', 18, 'Apple', None]

for str1 in L:
    if isinstance(str1, str):
        print("============>>>", str1.lower())
