# -*- coding: utf-8 -*-
"""
    fib
"""

import sys

maxNum = int(sys.argv[1])

if maxNum <= 0:
    raise ValueError('Width must be bigger than 0 !')

# 斐波纳契数列 正确答案 [1, 1, 2, 3, 5, 8, 13, 21, 34]
def fib(maxNum, i=0, j=1):
    if j < maxNum:
        print(j)
        tmp = i
        i = j
        j = tmp + j
        fib(maxNum, i, j)

fib(maxNum)