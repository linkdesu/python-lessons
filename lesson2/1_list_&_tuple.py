# -*- coding: utf-8 -*-
"""
    list_&_tuple
"""

# ==== list ====

# 声明 list 的方法
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
# list([iterable])
list3 = list("abcd")

# list 自带的一些方法
list1.append(4)
list1.extend([4, 5, 6])

# 引用赋值
list1 = [1, 2, 3]
list2 = list1
list2[1] = 5

print(list1, list2)


# ==== tuple ====

# 声明 tuple 的方法
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# tuple([iterable])
tuple3 = tuple("abcd")
