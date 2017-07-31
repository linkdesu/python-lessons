# -*- coding: utf-8 -*-
"""
    for
"""

# for i in range(10):
#     if i == 0:
#         print("Your input is 0")
#     else:
#         if i % 5 == 0:
#             print("%d is a multiple of 5" % i)
#         elif i % 2 > 0:
#             print("%d is an odd number." % i)    1
#         else:
#             print("%d is an even number." % i)

# container = []
# for i in range(10):
#     container.clear()
#     for j in range(10):
#         container.append(str(i) + str(j))            1
    # print(container)

# 斐波纳契数列 正确答案 [1, 1, 2, 3, 5, 8, 13, 21, 34]
answer = []
num2 = 0
num3_current = 1
while num3_current < 50:
    answer.append(num3_current)
    num1 = num2
    num2 = num3_current
    num3_current = num1 + num2
print(answer)