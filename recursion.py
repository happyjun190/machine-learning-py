#!/usr/bin/env python
# -*- coding: utf-8 -*-

def recursion(n=10):

    print("===>", n)
    if n < 1:
        return 0
    if n == 1:
        return 1
    return n * recursion(n-1)

def recursion2(n, m):
    if n<1:
        return 0
    if n==1:
        return m
    return recursion2(n-1, n*m)

print(recursion2(1000, 1))

