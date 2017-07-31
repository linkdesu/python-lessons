# -*- coding: utf-8 -*-
"""
    range
"""

a = range(10)
print("a: ", a)

# range(stop)
b = list(range(10))
print("b: ", b)

# range(start, stop)
c = list(range(1, 11))
print("c: ", c)

# range(start, stop[, step])
d = list(range(1, 11, 2))
print("d: ", d)

e = list(range(0, -10, -1))
print("e: ", e)