#!/usr/bin/env python3
#coding=utf-8

'SafeBase64Decode'

__author='Jyh'

import base64

def safe_base64_decode(s):
	n = len(s) % 4
	if n == 0:
		print(base64.urlsafe_b64decode(s))
	else:
		for i in range(4-n):
			s = s + "="
		print(base64.urlsafe_b64decode(s))

s = input('input the str')
safe_base64_decode(s)
