#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 12/22/20 4:18 PM
#@Author: Haoxin Shi
#@File  : ipR.py

from IPy import IP
xip = input('input ip:\n')

with open("Agoogleip.txt", "r") as f:
    for line in f.readlines():
        if (xip in IP(line)):
            print('This ip is on GoogleCloudRange!')

with open("Aawsip.txt", "r") as ff:
    for line in ff.readlines():
        if (xip in IP(line)):
            print('This ip is on AWSRange!')

with open("Aazureip.txt", "r") as fff:
    for line in fff.readlines():
        if (xip in IP(line)):
            print('This ip is on AzureRange!')