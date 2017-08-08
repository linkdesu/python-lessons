# -*- coding: utf-8 -*-
"""
    2_practice_function
"""

from collections import Iterable
from math import floor

# 自己实现一个求和函数。

# 自己实现一个求最大值或最小值的函数。

# def my_max(num, *rest_nums):
#     ret = 0
#     if isinstance(num, Iterable):
#         for i in num:
#             if i > ret:
#                 ret = i
#     else:
#         ret = num
#         for i in rest_nums:
#             if i > ret:
#                 ret = i
#     return ret
# print("my_max: ", my_max(5, 2, 3, 4))


# 再一次，尝试用函数的递归特性实现一个函数，它能够输出特定范围内的斐波那契数列。

# def fib(maxNum, i=0, j=1):
#     if j < maxNum:
#         print(j)
#         tmp = i
#         i = j
#         j = tmp + j
#         fib(maxNum, i, j)
# fib(50)


# 实现一个函数能够输出 * 组成的菱形。

# def draw(width, i=1, align='left'):
#     asterisk = ''
#     if (i < width):
#         if align == 'right':
#             for j in range(width - i):
#                 asterisk += ' '
#         elif align == 'center':
#             for j in range(floor((width - i) / 2)):
#                 asterisk += ' '
#
#         for j in range(i):
#             asterisk += '*'
#         print("%s" % asterisk)
#         draw(width, i + 2, align)
#         print("%s" % asterisk)
#
#     else:
#         for j in range(i):
#             asterisk += '*'
#         print("%s" % asterisk)
# draw(9, align='center')