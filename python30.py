#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2016/1/28
@author: yopoing
功能描述
"""
from mydecorator import write_log, use_time

@use_time
@write_log(call_time=False)
def func1():
    print 'i am func1, pay module'

# @write_log
# def func2():
#     print 'i am func2, reg module'
#
# @write_log
# def func3(arg):
#     print 'i am func3, login module'
#
@use_time
@write_log(call_time=False)
def func4(arg1, arg2=None):
    print 'i am func4, xx module'

# @write_log
# def func5(*args, **kwargs):
#     print 'i am func5, yy module'

# func1 = write_log(func1)
# func2 = write_log(func2)

func4('sss', 'fffdd')