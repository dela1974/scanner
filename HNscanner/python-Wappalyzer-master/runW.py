#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2/1/21 4:31 PM
#@Author: Haoxin Shi
#@File  : runW.py

from Wappalyzer import Wappalyzer, WebPage
import outputall

webpage = WebPage.new_from_url('http://aws.com')
wappalyzer = Wappalyzer.latest()
#print(wappalyzer.analyze(webpage))
#print(wappalyzer.analyze_with_categories(webpage))
a = wappalyzer.analyze_with_categories(webpage)
dict_a = dict(a)
outputall.outputall(dict_a)