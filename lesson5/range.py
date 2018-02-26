# -*- coding: utf-8 -*-
"""
    range
"""

# ==== 基础 ====

print(range(10))

# range(start, stop)
c = list(range(1, 11))
print("c: ", c)

# range(start, stop[, step])
d = list(range(1, 11, 2))
print("d: ", d)

e = list(range(0, -10, -1))
print("e: ", e)

# ==== 深入 ====

# range 函数返回的是一个可遍历的 Range 对象。
a = range(10)
print("a: ", a)

# 使用 list 函数可以将 Range 对象转为 List 对象，不过并没有这样的必要。
b = list(range(10))
print("b: ", b)