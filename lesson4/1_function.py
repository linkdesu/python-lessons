# -*- coding: utf-8 -*-
"""
    function
    Built-in Functions: https://docs.python.org/3/library/functions.html
"""

# 函数的调用

abs(-10)

max(7, 3)
max([1, 2, 3, 4, 5])

range(10)
range(1, 11)


# 函数的声明

def hello_world():
    print('hello world')

def empty_func():
    pass


# 函数的参数

def arg_test(a, b, c=1, d='test', *args, **kw):
    print('a: ', a)
    print('b: ', b)
    print('c: ', c)
    print('d: ', d)
    print('args: ', args)
    print('kw: ', kw)


# 函数的递归(recursive)

def re_func(a):
    if a < 10:
        print('In: ', a)
        b = re_func(a + 1)
        print('Out: ', a)
        return b
    else:
        print('End: ', a)
        return a
print(re_func(1))

