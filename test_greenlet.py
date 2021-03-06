# coding:utf-8
'''
greenlet
线程下的微线程
相当于一个代码块，可由用户指定何时执行某个微线程

switch(...):
    切换到此微线程并执行
    如果此微线程已结束，则返回给定的参数
    # 当第一次切换到微线程时，switch的参数会传递给执行函数
    以后切换到此微线程的参数则不会再被执行函数接收

throw(...):
    抛出异常 默认抛出 greenlet.GreenletExit()
    可指定异常 throw(IOError)

getcurrent()
    获取当前所在微线程

dead:
    微线程是否已结束

parent:
    每一个greenlet都有一个父，当导入greenlet模块时，会默认创建一个根父，此时新建的greenlet都已根为父，当greenlet死掉后，执行进程将返回到父greenlet
run:
    switch() 就开始执行run,执行注册的函数,greenlet启动后此属性将不存在

'''
from greenlet import greenlet
'''
class greenlet(__builtin__.object)
 |  greenlet(run=None, parent=None) -> greenlet
'''


def test1():
    print(12)
    gr2.switch("gr2's args")
    print(34)


def test2(args):
    print(56)
    print(args)
    gr1.switch()
    print(78)
    print(args)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
print("i am gr1: %s"%gr1)
print("i am gr2: %s"%gr2)
print("gr2.parent: %s"% gr2.parent)

gr1.switch()
print("gr1.dead: %s"%gr1.dead)
print("gr2.dead: %s"%gr2.dead)
print("切换回 gr2")
gr2.switch("不接收的参数")
print("gr2.dead: %s"%gr2.dead)
