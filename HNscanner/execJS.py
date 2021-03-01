#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 12/29/20 10:56 AM
#@Author: Haoxin Shi
#@File  : execJS.py
import execjs


# 执行本地的js

# def get_js():
#     # f = open("D:/WorkSpace/MyWorkSpace/jsdemo/js/des_rsa.js",'r',encoding='UTF-8')
#     f = open("./wappalyzer/src/drivers/npm/cli.js", 'r', encoding='UTF-8')
#     line = f.readline()
#     htmlstr = ''
#     while line:
#         htmlstr = htmlstr + line
#         line = f.readline()
#     return htmlstr


# with open('./wappalyzer/src/drivers/npm/wappalyzer.js') as f:
#     jsdata = f.read()
#
# ctx = execjs.compile(jsdata)
# res = ctx.call('Wappalyzer','www.baidu.com')

import js2py

data=open('./wappalyzer/src/drivers/npm/wappalyzer.js','r',encoding= 'utf8').read()
print(type(data))
data=js2py.eval_js(data)
print(data('baidu.com'))
