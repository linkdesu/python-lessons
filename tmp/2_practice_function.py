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
# 方法之一：
# def draw(width, i=1, align='left'):
#     asterisk = ''
#     if i < width:
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

# 方法之二：
# def draw_asterisk(num, offset = 0):
#     '''
#     绘制 * 字符串
#     :param num: * 字符的个数
#     :param offset: * 字符向右的偏移量，每个单位为一个空格
#     :return: 由 n 个空格和 m 个 * 号组成的字符串
#     '''
#     asterisk = ''
#     for i in range(num):
#         # 根据 num 绘制 * 号
#         asterisk += '*'
#     for j in range(offset):
#         # 根据 offset 在 * 号前面绘制空格
#         asterisk = ' ' + asterisk
#     return asterisk
#
# def draw(width, i=1, align='left'):
#     '''
#     用 * 号绘制图形
#     :param width: 图形最大宽度
#     :param i: 递归层数，默认从 1 开始
#     :param align: * 号对齐方式
#     :return:
#     '''
#     asterisk = ''
#     if i < width:
#         # 递归层数未到最大
#         if align == 'right':
#             # 右对齐
#             asterisk = draw_asterisk(i, width - i)
#         elif align == 'center':
#             # 居中对齐
#             asterisk = draw_asterisk(i, floor((width - i) / 2))
#         else:
#             # 左对齐
#             asterisk = draw_asterisk(i)
#
#         print(asterisk)
#         draw(width, i + 2, align)
#         print(asterisk)
#
#     else:
#         # 递归层数达到最大
#         asterisk = draw_asterisk(i)
#         print(asterisk)
# draw(9, align='center')