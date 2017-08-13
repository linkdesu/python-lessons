# -*- coding: utf-8 -*-
"""
    4_practice_generator
"""

# 实现一个生成器，只返回 100000 - 999999 以内的整数。
# gen = (x for x in range(100000, 1000000))
# for i in range(10):
#     print(next(gen))

# 实现一个生成器，只返回 1 - 1000 以内的，3的倍数、5的倍数。
# gen = (x for x in range(1, 10001) if x % 3 == 0 or x % 5 == 0)
# for i in range(10):
#     print(next(gen))

# 实现一个生成器，只返回斐波那契数列类的整数。

# def fibonacci(max_number):
#     num2 = 0
#     num3_current = 1
#     while num3_current < max_number:
#         yield num3_current
#         num1 = num2
#         num2 = num3_current
#         num3_current = num1 + num3_current
#
# for i in fibonacci(50):
#     print(i)