# Checkerboard
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

def setup():
    size(640, 360)

def draw():
    background(0)
    # stroke(255)
    spacing = 40
    count_x = 0  # count column number
    count_y = 0  # count row number

    for x in range(0, int(width) + 1, int(spacing)):
        for y in range(0, int(height) + 1, int(spacing)):
            # %(modulo) calculates the remainder when one number is divided by another.
            # If the col is even and the row is odd OR
            # If the col is odd and the row is even fill white
            if ((count_x % 2 == 0 and count_y % 2 == 1) or (count_x % 2 == 1 and count_y % 2 == 0)):
                fill(255)
            else:
                fill(0)
            rect(x, y, spacing, spacing)
            count_y += 1
        count_x += 1

run()
