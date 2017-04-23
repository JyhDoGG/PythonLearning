#!/usr/bin/env python3
#coding=utf-8

import functools

def log(text):
    if isinstance(text, str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s()' %(text, func.__name__))
                print('Begin call')
                func(*args, **kw)
                print('End call')
            return wrapper
        return decorator
    else:
        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('excute %s()' %  text.__name__)
            print('Begin call')
            text(*args, **kw)
            print('End call')
        return wrapper



@log
def now():
    print('2017-04-23')

@log('Excute')
def now_1():
    print('2017-04-23')

if __name__=='__main__':
    now()
    now_1()