#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 12/22/20 2:48 PM
#@Author: Haoxin Shi
#@File  : ip.py

import re
import json
import IPy


#pat = re.compile(r'(([0,1]?\d{1,2}|2([0-4][0-9]|5[0-5]))(\.([0,1]?\d{1,2}|2([0-4][0-9]|5[0-5]))){3}(/([0,1]?\d{1,2}|2([0-4][0-9]|5[0-5]))))')
pat = re.compile(r'\d+.\d+.\d+.\d+/\d+')
with open('azureip.json', 'r') as f:
    with open("Aazureip.txt", "w") as fp:
        for line in f.readlines():
            if(pat.search(line)!=None):
                #print(pat.findall(line))
                #with open("Agoogleip.txt", "w") as fp:
                    fp.writelines(pat.findall(line))
                    fp.write('\n')