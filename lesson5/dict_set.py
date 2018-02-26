# -*- coding: utf-8 -*-
"""
    dict_&_set
"""

# ==== dict ====
# https://docs.python.org/3.6/library/stdtypes.html#mapping-types-dict

# 声明 dict 的方法
dict1 = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
dict2 = {'Michael': 'A', 'Bob': 'C', 'Tracy': 'B'}
dict3 = dict(Michael=95, Bob=75, Tracy=85)
print(dict1)

# 获取 dict 指定元素的方法
# print(dict1['Michael'])

# 检测 dict 是否含有特定键的方法
# print('Michael' in dict1, 'NotExist' in dict1)

# 获取不确定是否存在的 dict 值的方法
# print(dict1['NotExist'])
# print(dict1.get('NotExist', 0))

# 通过变量动态的访问不同的键
# key1 = 'Bob'
# print(dict1[key1])

# 引用赋值
# dict2 = dict1
# dict2['Michael'] = 70
#
# print(dict1, dict2)


# ==== set ====
# 声明 set 的方法
# set1 = {'Michael', 'Bob', 'Tracy'}
# print(set1)

# 修改 set 的方法
# set1.add('Tracy')
# set1.add('Link')
# print(set1)
