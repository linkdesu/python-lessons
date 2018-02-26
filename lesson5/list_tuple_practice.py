# -*- coding: utf-8 -*-
"""
    4_practice_list_&_tuple
"""

# 声明一个 10 个元素的 list/tuple 。


# 声明一个 1 - 50 的 list/tuple 。


# a 为 1 - 10 的 list ，请获取第 1、5、10 个元素。


# a 为 1 - 10 的 list ，截取出开始 3 个数，截取出最后 3 个数。


# a 为 1 - 10 的 list ，截取出奇数，截取出偶数。


# 查文档了解 list 和 tuple 所有的方法。


# 下面几行代码会生成一个包含随机数的 list ，结合循环、逻辑判断的知识写一段小程序，找出该 list 中最大的数、最小的数。
# from random import randint
# a = [randint(1, 100) for i in range(10)]
# print(a)


# 下面几行代码会生成一个包含随机数的 list ，使用 list.sort() 就可以对其进行排序，但这里请尝试自己写一段小程序实现和 sort 同样的排序效果。
# from random import randint
# a = [randint(1, 100) for i in range(10)]
# print('随机产生的结果：', a)
# a.sort()
# print('排序后的结果：', a)

# 排序算法：http://python.jobbole.com/82270/
# 冒泡排序：
# length = len(a)
# for i in range(length):
#     for j in range(i + 1, length):
#         if a[i] > a[j]:
#             a[j], a[i] = a[i], a[j]
# print(a)


# 下面几行代码会生成一个包含 0 - 9 的随机顺序的 list ，使用 a.sort() 即可对该 list 进行排序，
# 但是现在请尝试在不实用 a.sort() 方法的情况下对其进行排序。

# 引入 random 模块
import random
# 生成一个 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 的 list
a = list(range(10))
# 将其打乱，因为 random.shuffle 会直接修改容器内部的数据，所以这里不再需要复制
random.shuffle(a)
# 打印出来将看到一个乱序的 list
# print(a)