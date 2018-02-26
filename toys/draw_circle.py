# -*- coding: utf-8 -*-
"""
    draw_circle
"""

import turtle

turtle.speed(100)

count = int(input('How many circle do you want: '))

for i in range(0, count):
    radius = (i + 1) * 20
    turtle.circle(radius)

turtle.exitonclick()