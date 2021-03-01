#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2/22/21 11:57 AM
#@Author: Haoxin Shi
#@File  : inputall.py

import re
import json
import IPy
import modCh
import time

def banner():
    print("""\033[96m
 1) DNS Lookup                 13) Host DNS Finder
 2) Whois Lookup               14) Reserve IP Lookup
 3) GeoIP Lookup               15) Email Gathering (use Infoga)
 4) Subnet Lookup              16) Subdomain listing (use Sublist3r)
 5) Port Scanner               17) Find Admin login site (use Breacher)
 6) Page Links                 18) Check and Bypass CloudFlare (use HatCloud)
 7) Zone Transfer              19) Cloud Ip Range Detection
 8) HTTP Header                20) Host Info Scanner (use WhatWeb)
 9) Host Finder                21) Cloud App Detection
 10) IP-Locator                22) Banner grabbing
 11) Find Shared DNS Servers   23) Exit
 12) Get Robots.txt""")
    print()
aa = 'ip'
bb = '10'
#pat = re.compile(r'(([0,1]?\d{1,2}|2([0-4][0-9]|5[0-5]))(\.([0,1]?\d{1,2}|2([0-4][0-9]|5[0-5]))){3}(/([0,1]?\d{1,2}|2([0-4][0-9]|5[0-5]))))')
pat = re.compile(r'\d+.\d+.\d+.\d')
with open('ipinput.txt', 'r') as f:
    for line in f.readlines():
        if(pat.search(line)!=None):
            #print('ip: ', line)
            cc = line.strip('\n')
            print('\033[91m-----------------------------------------------')
            modCh.iseeverything(aa,bb,cc)
            #time.sleep(1)