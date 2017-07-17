# -*- coding: utf-8 -*-
"""
    while
"""

import sys

try:

    i = 0
    while True:
        if i >= 3:
            print('Input too many times !')
            break
        i += 1

        text = input("Please input something: ")
        print("Your input is: ", text)

except KeyboardInterrupt:
    print("\nExit program")
    sys.exit(0)