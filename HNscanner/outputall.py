#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2/25/21 9:14 AM
#@Author: Haoxin Shi
#@File  : outputall.py

import json
def outputall(dict_var):
    print(json.dumps(dict_var, indent=2,sort_keys=True, ensure_ascii=False))
    with open("output.json", "w", encoding='utf-8') as f:
        # json.dump(dict_var, f)  # 写为一行
        json.dump(dict_var, f, indent=2, sort_keys=True, ensure_ascii=False)