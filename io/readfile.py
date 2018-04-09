#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

try:
    f = open("D:\pythonTest.txt",'r');
    for line in f.readlines():
        print(line.strip())
except Exception as e:
    logging.exception("读取文件异常:", e)
finally:
    print("读取结束")
    if f:
        f.close()
    else:
        print("f 已经关闭")

#with open('D:\pythonTest.txt', 'r') as f:
#    print(f.read())