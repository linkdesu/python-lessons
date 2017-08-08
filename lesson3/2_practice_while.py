# -*- coding: utf-8 -*-
"""
    2_practice_while
"""

# 从控制台接收三次输入，当输入第四次时退出，请自行 Google Python3 如何接收命令行输入。

# i = 0
# while True:
#     if i >= 3:
#         print('Input too many times !')
#         break
#     i += 1
#
#     text = input("Please input something: ")
#     print("Your input is: ", text)


# 遍历 1-10 的 list ，求每个数的平方的总和，公司为 y = x[0] * x[0] + x[1] * x[1] +... 。

# a = range(1, 11)
# total = 0
# i = 0
# while i < len(a):
#     total += a[i] * a[i]
#     i += 1
# print(total)


# 遍历下面两个 list ，求 a 中每个元素和 b 中每个元素相乘结果的总和，公式为 z = x[0] * y[0] + x[0] * y[1] +... x[1] * y[0] + x[1] * y[1] +... 。
a = list(range(1, 11, 2))
b = list(range(2, 11, 2))

# total = 0
# i = 0
# while i < len(a):
#     j = 0
#     while j < len(b):
#         total += a[i] * b[j]
#         j += 1
#     i += 1
# print(total)