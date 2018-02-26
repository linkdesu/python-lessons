# -*- coding: utf-8 -*-
"""
    slice
"""

# 声明一个后续使用的 list
a = list(range(1, 11))
print("a is: ", a)

# ==== 两个参数切片 ====
# a[start:stop]
# print("Slice 1 to 5: ", a[0:5], a[:5], a[:-5])
# print("Slice 5 to 10: ", a[5:10], a[5:], a[-5:])

# ==== 三个参数切片 ====
# a[start:stop:step]
# print("Slice with step: ", a[0::2])