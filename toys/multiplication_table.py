# -*- coding: utf-8 -*-
"""
    multiplication_table
"""

for i in range(1, 10):
    text = ''
    for j in range(1, i + 1):
        text = text + '%d x %d = %d | ' % (j, i, i * j)
    print(text)