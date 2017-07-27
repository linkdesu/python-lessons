# -*- coding: utf-8 -*-
"""
    spinner
"""

import time

def spinner():
    while True:
        for char in '|/-\\':
            print('[' + char + '] loading...', end='\r')
            time.sleep(0.1)
spinner()
