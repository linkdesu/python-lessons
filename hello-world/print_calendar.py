# -*- coding: utf-8 -*-
"""
    calendar
"""

import calendar

__author__ = "Linkdesu"
__email__ = "xieaolin@foxmail.com"

# To ask month and year from the user
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))