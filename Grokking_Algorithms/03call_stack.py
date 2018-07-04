# -*- coding:utf-8 -*-
"""This module is used to test call stack"""


# def greet(name):
#     print(name)
#     fun(name)
#     print('bye bye !!!')
#     bye()
#
#
# def fun(name):
#     print('how are you', name)
#
#
# def bye():
#     print('good bye')
#
#
# greet('feifei')

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(3))
