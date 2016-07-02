#!/usr/bin/env python3
#coding=utf-8

'Html Parser'

__author__ = 'Jyh'

from html.parser import HTMLParser

class MyParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.Events = {}
        self._tag = ''
        self._counter = 0
        
    def handle_starttag(self, tag, attrs):
        if attrs == [('class', 'event-title')]:
            self._tag = 'title'
        if tag == 'time':
            self._tag = 'time'
        if attrs == [('class', 'event-location')]:
            self._tag = 'location'

    def handle_data(self, data):
        if self._counter < 3:
            if self._tag == 'title':
                self.Events[self._counter] = {'title':data}
            if self._tag == 'time':
                self.Events[self._counter]['time'] = data
            if self._tag == 'location':
                self.Events[self._counter]['location'] = data
                self._counter += 1
        self._tag = ''
    def PrintEvents(self):
        for k in self.Events:
            print('【title】:%s 【time】:%s 【location】:%s' %(self.Events[k]['title'], self.Events[k]['time'], self.Events[k]['location']))
       

if __name__ == '__main__':
    with open('test.html', 'r', encoding='UTF-8') as f:  #测试html为https://www.python.org/events/python-events/
        html = f.read()
    
parser = MyParser()
parser.feed(html)
parser.PrintEvents()