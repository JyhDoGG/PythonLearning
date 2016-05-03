#!/usr/bin/env python3
#coding=utf-8

__author__='Jyh'

#将字符串转换为浮点数

from functools import reduce

Char2Num = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '.':-1}

def str2float(s):
    num = map(lambda x: Char2Num[x], s)
    point = 0
    def fn(x, y):
        nonlocal point
        if y == -1:
            point = 1
            return x
        if point == 0:
            return 10 * x + y
        else:
            point = point / 10
            return x + y * point
    return reduce(fn, num, 0.0)

print(str2float('123.456'))   
