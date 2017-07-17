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

# 斐波纳契数列
def fibonacci(max_number):
    step = 0
    current = 1
    while current < max_number:
        yield current
        tmp = step
        step = current
        current = tmp + current
    return 'done'
# print(fibonacci(10))

for i in fibonacci(10):
    print(i)