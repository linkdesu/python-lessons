# -*- coding: utf-8 -*-
"""
    list_&_tuple
"""

# ==== list ====

list1 = [1, 2, 3]
list2 = [4, 5, 6]
# list([iterable])
list3 = list("abcd")

print(list1 + list2)
print(list1 * 2)
print(list3)
print(1 in list1, 1 in list2)

# a_list.append(4)
# a_list.extend([4, 5, 6])

# ==== tuple ====

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
# tuple([iterable])
tuple3 = tuple("abcd")

print(tuple1 + tuple2)
print(tuple1 * 2)
print(tuple3)
print(1 in tuple1, 1 in tuple2)
