def f(x):
    return x*x


l1 = list(range(1,100))
l2 = list(map(f, l1))
print(l2)


def fr(x, y):
    return x*10+y;

from functools import reduce
print(reduce(fr, [1,2,3,4,5,6,7]))


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]
print(list(map(char2num, '13579')))
print(reduce(fr, map(char2num, '13579')))
