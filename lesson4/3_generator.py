# -*- coding: utf-8 -*-
"""
    generator
"""

# range 对象
list1 = range(0, 10)
print(list1)

# 列表生成式即 List Comprehensions
list2 = [x for x in range(1, 11)]
print(list2)

list3 = [x for x in range(1, 11) if x % 2 == 0]
print(list3)

list4 = [str(x) + str(y) for x in range(3) for y in range(3)]
print(list4)

# 生成器
generator1 = (x * x for x in range(1, 11))
print(generator1)

generator2 = (x for x in range(1, 11) if x % 2 == 0)
print(generator2)

generator3 = (str(x) + str(y) for x in range(3) for y in range(3))
print(generator3)

# 更复杂的生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
print(fib, fib(10))

for i in fib(10):
    print(i)