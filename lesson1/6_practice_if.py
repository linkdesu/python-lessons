# -*- coding: utf-8 -*-
"""
    practice_if
"""

# a 的值是多少？
a = 1
if True:
    a = 9

# a 的值是多少？
a = 1
if False:
    a = 9

# a 的值是多少？
a = 3
if a > -1 and a == 10:
    a = 5

# a 的值是多少？
a = 3
if a > 2 or a < 5:
    a = 5

# a 的值是多少？
a = 3
if a > 2 or a < 5:
    b = 1 + 1
    a = a + b
    
a = a * 10

# 首先判断 num 是否是 5 的倍数，如果不是，再判断 num 是奇数，还是偶数。
num = 99
