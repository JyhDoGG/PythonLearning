#!/usr/bin/env python3
#coding=utf-8

'yanghuisanjiao'

__auther__='Jyh'

#杨辉三角

def fn(num):
    L = [1]
    n = 0
    while n < num:
	    print(L) 
	    L.append(0)
	    L = [L[n] + L[n-1] for n in range(len(L))]
	    n = n + 1
		


fn(10)
