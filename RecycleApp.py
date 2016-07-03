#!/usr/bin/env python3
#coding=utf-8

'Auto Recycle Application '

__author__ = 'Jyh'

import http.client
import time
import os
import threading

def TestWeb(url):       #测试网站是否OK
    conn = http.client.HTTPConnection ('ce.sysu.edu.cn')
    conn.request('GET', url)
    r = conn.getresponse()
    x = r.status    #获得网页状态码
    counter = 0
    while counter < 3:
        if x == 200:
            counter = 0
            time.sleep(60)
        else:
            counter += 1
            time.sleep(30)
    if counter >= 3:   #如果连续三次状态码不是200，回收应用程序池
        RecycleAPP(url)
        
def RecycleAPP(url):        #回收应用程序池
    dict = {'/':'ce.chem2015', '/hope/':'ce.hope'}  #网站对应的应用程序名
    commend1 = 'c:\windows\system32\inetsrv\AppCmd.exe stop apppool /apppool.name:"%s"' %dict[url]
    commend2 = 'c:\windows\system32\inetsrv\AppCmd.exe start apppool /apppool.name:"%s"' %dict[url]
    os.system(commend1)
    time.sleep(30)
    os.system(commend2)
    
t1 = threading.Thread(target=TestWeb, args=('/',)) 
t2 = threading.Thread(target=TestWeb, args=('/hope/',)) 
t1.start()
t2.start()
