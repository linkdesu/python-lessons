# -*- coding: utf-8 -*-
"""
    for
"""

for i in range(10):
    if i == 0:
        print("Your input is 0")
    else:
        if i % 5 == 0:
            print("%d is a multiple of 5" % i)
        elif i % 2 > 0:
            print("%d is an odd number." % i)
        else:
            print("%d is an even number." % i)

container = []
for i in range(10):
    container.clear()
    for j in range(10):
        container.append(str(i) + str(j))
    print(container)

# 斐波纳契数列 正确答案 [1, 1, 2, 3, 5, 8, 13, 21, 34]
answer = []
step = 0
current = 1
while current < 50:
    answer.append(current)
    tmp = step
    step = current
    current = tmp + current
print(answer)