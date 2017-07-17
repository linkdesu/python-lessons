# -*- coding: utf-8 -*-
"""
    dict_&_set
"""

# ==== dict ====

dict1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(dict1)

print(dict1['Michael'])
print('Michael' in dict1, 'NotExist' in dict1)
# print(dict1['NotExist'])
print(dict1.get('NotExist', 0))

key1 = 'Bob'
print(dict1[key1])


# ==== set ====
set1 = {'Michael', 'Bob', 'Tracy'}
print(set1)

set1.add('Tracy')
set1.add('Link')
print(set1)
