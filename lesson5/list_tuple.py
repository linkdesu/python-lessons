# -*- coding: utf-8 -*-
"""
    list_&_tuple
"""

# ==== list ====
# https://docs.python.org/3.6/library/stdtypes.html#sequence-types-list-tuple-range

# '''

# 声明 list 的方法
list1 = [1, 2, 3]
list2 = ['a', 1, True]
list3 = list("abcd")
# print(list3)


# list 自带的一些方法
# del list1[0]
# print(list1)
# list1.insert(0, 4)
# list1.extend([4, 5, 6])
# print(list1)

# 引用赋值
list1 = [1, 2, 3]
list2 = list1
list2[0] = 5
print(list1, list2)

# '''

# ==== tuple ====

# 声明 tuple 的方法
tuple1 = (1, 2, 3)
tuple2 = ('a', 1, True)
tuple3 = tuple("abcd")

# tuple1[0] = 5
# tuple1.append(4)
# tuple1 = (4, 5, 6)
# print(tuple1)
