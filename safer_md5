#!/usr/bin/env python3
#coding=utf-8

'safer MD5'

__author__ = 'Jyh'

import hashlib

def md5(s):                        #获得MD5值
    md5 = hashlib.md5()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()
	 
db = {}
def register(username, password):  #记录到数据库 
    db[username] = md5(password + username + 'the-Salt')	
	
def log_in(username, password):
    if username not in db:         #判断是否为新用户
	    register(username, password)
	    print('register finished')
    elif db[username] == md5(password + username + 'the-Salt'):
        print('Welcome! Mr.%s' %username[0])
    else:
        print('Your password is wrong. Please try again.')	


#test
#log_in('jyh', '123')
#log_in('jyh', '234')
#log_in('jyh', '123')
#log_in('123', 'jyh')

		
username = input('Please input your username')
password = input('Please input your password')
log_in(username, password)
