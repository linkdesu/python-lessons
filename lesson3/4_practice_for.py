# -*- coding: utf-8 -*-
"""
    4_practice_for
"""

# 声明一个 1 - 10 的 list ，并遍历其中每个元素，首先判断元素是否为 5 的倍数，如果不是再判断元素是奇数还是偶数。

# 在命令行中生成下面样式的矩阵：
# ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
# ['10', '11', '12', '13', '14', '15', '16', '17', '18', '19']
# ['20', '21', '22', '23', '24', '25', '26', '27', '28', '29']
# ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39']
# ['40', '41', '42', '43', '44', '45', '46', '47', '48', '49']
# ['50', '51', '52', '53', '54', '55', '56', '57', '58', '59']
# ['60', '61', '62', '63', '64', '65', '66', '67', '68', '69']
# ['70', '71', '72', '73', '74', '75', '76', '77', '78', '79']
# ['80', '81', '82', '83', '84', '85', '86', '87', '88', '89']
# ['90', '91', '92', '93', '94', '95', '96', '97', '98', '99']

# container = []
# for i in range(10):
#     container.clear()
#     for j in range(10):
#         container.append(str(i) + str(j))
#     print(container)

# 生成 50 以内的斐波纳契数列，正确答案为 [1, 1, 2, 3, 5, 8, 13, 21, 34]。

# answer = []
# num2 = 0
# num3_current = 1
# while num3_current < 50:
#     answer.append(num3_current)
#     num1 = num2
#     num2 = num3_current
#     num3_current = num1 + num2
# print(answer)