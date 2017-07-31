# -*- coding: utf-8 -*-
"""
    generator
"""

list1 = range(0, 10)
print(list1)

list2 = [range(0, 10)]
print(list2)

list3 = [x * x for x in range(1, 11)]
print(list3)

list4 = (x * x for x in range(1, 11))
print(list4)
