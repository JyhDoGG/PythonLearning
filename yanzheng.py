#!/usr/bin/env python3
#coding=utf-8

'ZhengzeYanzhengEmail'

__auther__ = 'Jyh'

import re

yanzheng = re.compile(r'^((\w)+(\.\w)*)@(\w)+((\.\w{2,3}){1,3})$')

r = input('Please input your Email.')

if yanzheng.match(r):
    print('OK')
    x = yanzheng.match(r).group(1)
    print('username =', x)
else:
    print('False')