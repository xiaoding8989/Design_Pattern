# usr/bin/env python
# -*-coding:utf-8 -*-

class Singleton(object):
    __instance=None
    def __new__(cls, *args, **kwargs):
        if Singleton.__instance is None:
            Singleton.__instance=object.__new__(cls,*args,**kwargs)
        return Singleton.__instance

s1=Singleton()
s2=Singleton()
s1.a=900
print s1.a,s2.a
print id(s1)
print id(s2)
print s1==s2