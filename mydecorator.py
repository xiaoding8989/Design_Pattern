#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on 2016/1/28
@author: yopoing
功能描述
"""

def write_log(call_time):
    '''
    写函数调用日志的装饰器
    :param call_time:
    :return:
    '''
    '''
    :param call_time:
    :return:
    '''
    def wrapper(func):
        def _write_log(*args, **kwargs):

            import logging
            import datetime
            import inspect

            logging.basicConfig(level=logging.DEBUG,
                                filename='python30.log')

            func(*args, **kwargs)
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            all_args = inspect.getargspec(func)
            log_info = '函数名:'+func.func_name+', 参数:'+str(all_args)
            if call_time:
                log_info += '，调用时间：'+now
            logging.debug(log_info)
        return _write_log
    return wrapper

def use_time(func):
    '''
    计算函数执行时间
    :param func:
    :return:
    '''
    def wrapper(*args, **kwargs):

        import time

        start = time.clock()
        func(*args, **kwargs)
        end = time.clock()
        print 'use time: '+str(end-start)
    return wrapper
