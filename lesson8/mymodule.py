# -*- coding: utf-8 -*-
"""
    mymodule
"""

from enum import Enum

__author__ = "Linkdesu"
__email__ = "xxx@xxx.com"


my_var = 123

__pri_my_var = 123

def hello_world():
    print('hello world')

def __pri_hello_world():
    print('hello world')


def fib2(n):
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

class Color(Enum):
    WHITE = 1
    BLACK = 2
    BLUE = 3
    RED = 4