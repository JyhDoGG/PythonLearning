#!/usr/bin/env python3
#coding=utf-8

'find file with s in current dir and sub-dir'

__auther__='Jyh'

import os

def fn(d, s):
    for x in os.listdir(d):
        path = os.path.join(d,x)
        if os.path.isfile(path) and s in x:
            print('FileName:%s, RelativePath:%s' %(x, path))
        if os.path.isdir(path):
            fn(path, s)
			
	
s = input('input the key')
fn('.', s)