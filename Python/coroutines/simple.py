# -*- coding:utf-8 -*-
"""协程的简单演示"""

# def simple_coroutine():
#     print('start')
#     x = yield
#     print('receive:', x)
#
#
# coro = simple_coroutine()
# print(coro)
# next(coro)  # 激活协程
# coro.send(42)

from inspect import getgeneratorstate


def simple_coroutine(a):
    print('start: a =', a)
    b = yield a
    print('receive: b =', b)
    c = yield a + b
    print('receive: c =', c)


coro = simple_coroutine(14)
print(getgeneratorstate(coro))
next(coro)  # 激活协程
print(getgeneratorstate(coro))
try:
    coro.send(28)
    coro.send(99)
except StopIteration as e:
    print('Exception: %s' % e)
print(getgeneratorstate(coro))
