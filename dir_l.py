#!/usr/bin/env python3
#coding=utf-8

'a dir -l model'

__auther__='Jyh'

import os

def dir_l(path):
    print([x for x in os.listdir(path)])
	
path = input('input the path')
dir_l(path)