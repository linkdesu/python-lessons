# -*- coding: utf-8 -*-
"""
    asterisk
"""

import sys

width = int(sys.argv[1])
align = sys.argv[2]

if width <= 0:
    raise ValueError('Width must be bigger than 0 !')

def draw(width, i=1, align='left'):
    asterisk = ''
    if (i < width):
        if align == 'right':
            for j in range(width - i):
                asterisk += ' '
        elif align == 'center':
            for j in range(floor((width - i) / 2)):
                asterisk += ' '

        for j in range(i):
            asterisk += '*'
        print("%s" % asterisk)
        draw(width, i + 2, align)
        print("%s" % asterisk)

    else:
        for j in range(i):
            asterisk += '*'
        print("%s" % asterisk)

draw(width, align=align)