# -*- coding: utf-8 -*-
"""
    slice
"""

a = list(range(1, 11))
print("a is: ", a)

# a[start:stop]
print("Slice 1 to 5: ", a[0:5], a[:5], a[:-5])
print("Slice 5 to 10: ", a[5:10], a[5:], a[-5:])

# a[start:stop:step]
print("Slice with step: ", a[0::2])