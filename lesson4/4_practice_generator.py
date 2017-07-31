# -*- coding: utf-8 -*-
"""
    4_practice_generator
"""


# 实现一个 generator ，它能够用于获取一个斐波那契数列

# def fibonacci(max_number):
#     step = 0
#     current = 1
#     while current < max_number:
#         yield current
#         tmp = step
#         step = current
#         current = tmp + current
# for i in fibonacci(50):
#     print(i)