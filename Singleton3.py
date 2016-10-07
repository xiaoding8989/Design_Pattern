# usr/bin/env python
# -*-coding:utf-8 -*-
#方法二：装饰器

def singleton(cls, *args, **kwargs):
    instances={}
    def _singleton():
        if cls not in instances:
            instances[cls]=cls(*args, **kwargs)
    return _singleton

@singleton
class MyClass2():
    a = 1

m1 = MyClass2()
m2 = MyClass2()

#m1.a = 3
#print m1.a
# id  == is
print id(m1)
print id(m2)
print m1 == m2