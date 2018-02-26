# -*- coding: utf-8 -*-
"""
    1_class_object
"""

class Student:

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.__age = age

    def say_hello(self):
        print('Hello, Im ' + self.name + ', Im ' + str(self.__age))

link = Student('Link', 'm', 20)
steve = Student('Steve', 'male', 20)

link.say_hello()
steve.say_hello()

print('Hello, user ' + link.name)
# print('Hello, user ' + link.name + ' you are ' + link.__age)

