#!/usr/bin/env python3
#coding=utf-8

'print bmp size colors'

__author='Jyh'

import struct
import os.path

def bminfo(p):
	with open(p,'rb') as f: #打开文件p，并将前30字节写入s
		s = f.read(30)
	l = struct.unpack('<ccIIIIIIHH', s)
	path = os.path.split(p) #拆分文件的路径
	filename = path[-1] #获得文件名
	if l[0] == b'B' and l[1] == b'M': #判断是不是bmp位图
		print('%s is a bmp file' %filename)
		print('size = %d*%d, colors = %d' %(l[-4], l[-3], l[-1]))
	else:
		print('%s in not a bmp file' %filename)

p = input("input the file's path")
bminfo(p)