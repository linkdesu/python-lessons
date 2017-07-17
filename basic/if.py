# -*- coding: utf-8 -*-
"""
    if
"""

num = int(input("Enter a number: "))
if num == 0:
    print("Your input is 0")
else:
    if num % 5 == 0:
        print("%d is a multiple of 5" % num)
    elif num % 2 > 0:
        print("%d is an odd number." % num)
    else:
        print("%d is an even number." % num)