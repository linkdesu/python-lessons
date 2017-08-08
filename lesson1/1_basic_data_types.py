# -*- coding: utf-8 -*-
"""
    basic_data_types
"""

# 整型数据
type_int = 1
type_int = -1
print(type_int)

# 浮点型数据
type_float = 1.00
type_float = -1.00
print(type_float)

# 布尔型数据
type_bool_1 = True
type_bool_2 = False
print(type_bool_1)
print(type_bool_2)

# 字符串型数据，单双引号均可
type_string_s1 = 'hello world'
type_string_m1 = "hello world"

# 对于单双引号内含单双引号的情况要转义
type_string_s1 = 'hello \' world'
type_string_m1 = "hello \" world"

# \n \r \t \\ 等是有特殊含义的转义字符
type_string_s2 = 'hello\nworld'

# r 开头的字符串转义符都会被当做普通字符
type_string_s3 = r'hello\nworld'

# 多行字符串
type_string_s4 = '''hello
+ world
'''
