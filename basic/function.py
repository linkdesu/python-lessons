# -*- coding: utf-8 -*-
"""
    function
    Built-in Functions: https://docs.python.org/3/library/functions.html
"""

from collections import Iterable
from math import floor

print("abs: ", abs(10), abs(-10))

print("max: ", max(7, 3), max(7, 3, 5), max([7, 3, 5]))

print("min: ", min(7, 3), min(7, 3, 5), min([7, 3, 5]))

print("sum: ", sum([1, 2, 3, 4, 5]))

print("len: ", len([1, 2, 3, 4, 5]))

def my_max(num, *rest_nums):
    ret = 0
    if isinstance(num, Iterable):
        for i in num:
            if i > ret:
                ret = i
    else:
        ret = num
        for i in rest_nums:
            if i > ret:
                ret = i
    return ret
print("my_max: ", my_max(5, 2, 3, 4))

print('\n')
def draw(width, i = 1, align = 'left'):
    asterisk = ''
    if (i < width):
        if align == 'right':
            for j in range(width - i):
                asterisk += ' '
        elif align == 'center':
            for j in range(floor((width - i) / 2)):
                asterisk += ' '

        for j in range(i):
            asterisk += '*'
        print("%s" % asterisk)
        draw(width, i+2, align)
        print("%s" % asterisk)

    else:
        for j in range(i):
            asterisk += '*'
        print("%s" % asterisk)

draw(9, align='center')