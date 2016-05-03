#!/us/bin/env python3
#coding=utf-8

'str2timestamp'

__autho__='Jyh'

import re
from datetime import datetime, timezone, timedelta

def str2timestamp(dt_str, tz_str):
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    tz_re = re.compile(r'^(UTC)([\+|\-]\d+)(:00)$')  
    if tz_re.match(tz_str):
        h = tz_re.match(tz_str).group(2)
        dt.replace(tzinfo=timezone(timedelta(hours=int(h))))	
    print(dt.timestamp())
    print('UTC:' + h + ':00')

dt = input('input the datetime')
dz = input('input the datezone')

str2timestamp(dt, dz)	