# -*- coding: utf-8 -*-
"""
    turtle
"""

import turtle
from math import sin, cos, radians


# 设置屏幕大小
screen = turtle.Screen()
screen.title('齿轮梨 Python 实践课')
screen.setup(550, 550)

# 我就想任性的让这只为我画画的小乌龟也叫 Link
link = turtle.Turtle()
link.speed(100)

# '''
# 首先画出最外面的正方形
link.penup()
link.setpos(-250, -250)
link.pencolor('#4400CC')
link.pensize(5)
link.pendown()
for i in range(4):
    link.forward(500)
    link.left(90)


# 然后画出四个角的四个小圆
# 首先规定每个圆的半径为 30
circle_radius = 30
my_list = [200, -200]

for i in my_list:
    for j in my_list:
        link.penup()
        link.setpos(i, j - circle_radius)
        link.pencolor('#000000')
        link.pensize(5)
        link.pendown()
        link.circle(circle_radius)

# '''
# 绘制中间的大正八边形
# 首先规定其半径为 150
octagon_radius = 150
a = sin(radians(45 / 2)) * octagon_radius
b = cos(radians(45 / 2)) * octagon_radius

link.penup()
link.setpos(-a, -b)
link.pencolor('#4400CC')
link.pensize(5)
link.pendown()
for i in range(8):
    link.forward(sin(radians(45 / 2)) * octagon_radius * 2)
    link.left(360 / 8)

# '''
# 绘制内部圆心在原点上的小八边形
octagon_radius = 50

link.penup()
link.setpos(0, -50)
link.pencolor('#00AA22')
link.pensize(5)
link.pendown()
link.circle(octagon_radius, None, 8)


def circle(radius, pensize, color):
    if radius < 1:
        radius = 1

    link.penup()
    link.setpos(0, -radius)
    link.pencolor(color)
    link.pensize(pensize)
    link.pendown()
    link.circle(radius)

# '''
# 绘制出内部剩余的几个圆
radius = 40
circle(radius, 5, '#000000')
circle(radius - 10, 20, '#996637')
circle(radius - 20, 5, '#000000')
circle(radius - 30, 5, '#212a39')

# 每次画完屏幕就自动关闭，我希望它能够在我点击后才关闭，那么就 Exit on click
screen.exitonclick()
