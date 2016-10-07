# usr/bin/env python
# -*-coding:utf-8 -*-
# 方法1. 实现 __new__
# 绑定
# 如果 __instance 为None ,说明__instance没有实例化, -->实例化,并返回
# 反之 直接返回 __instance
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            orig=super(Singleton,cls)
            cls._instance=orig.__new__(cls, *args, **kwargs)
        return cls._instance
class MyClass(Singleton):
    a=1
m1 = MyClass()
m2 = MyClass()

m1.a = 3
print m1.a
# id  == is
print id(m1)
print id(m2)
print m1 == m2




















