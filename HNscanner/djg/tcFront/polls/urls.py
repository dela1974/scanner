#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2/2/21 11:33 AM
#@Author: Haoxin Shi
#@File  : urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]