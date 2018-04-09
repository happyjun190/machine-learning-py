#!/usr/bin/env python
# -*- coding: utf-8 -*-

g = (x*x for x in range(5))

print(next(g),next(g),next(g),next(g),next(g))

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b);
        a, b = b , a+b
        n = n + 1
    return "done"

fib(5)