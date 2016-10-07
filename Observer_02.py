# -*- coding:utf-8 -*-

# 观察者模式

# 模式特点：定义了一种一对多的关系，让多个观察对象同时监听一个主题对象，
# 当主题对象状态发生变化时会通知所有观察者。

# 程序实例：公司里有两种上班时趁老板不在时偷懒的员工：
# 看NBA的和看股票行情的，并且事先让老板秘书当老板出现时通知他们继续做手头上的工作。


# 观察者 -->抽象观察者
class Obserber:

    def __init__(self, strname, strsub):
        self.name = strname
        self.sub = strsub

    def Update(self):
        pass


# 具体观察者
class StockObserver(Obserber):
    def Update(self):
        print u'%s:%s,停止看股票,继续工作!'%(self.name, self.sub.action)


# 具体观察者
class NBAObserver(Obserber):
    def Update(self):
        print u'%s:%s,停止看股票,继续工作!'%(self.name, self.sub.action)


# 规则(主题) -->抽象
class SecretarytBase:

    def __init__(self):
        self.observer = []

    def Attach(self,new_observer):
        pass

    def deleteobserver(self,new_oberer):
        pass

    def Notify(self):
        pass


class Secretary(SecretarytBase):

    def Attach(self,new_observer):  # 添加
        self.observer.append(new_observer)

    def Notify(self):
        for p in self.observer:  # 2
            p.Update()

if __name__ == '__main__':
    p = Secretary()
    s1 = StockObserver('Tom', p)
    s2 = NBAObserver('Jack', p)
    p.Attach(s1)
    p.Attach(s2)
    p.action = "WARNING:BOSS"
    p.Notify()