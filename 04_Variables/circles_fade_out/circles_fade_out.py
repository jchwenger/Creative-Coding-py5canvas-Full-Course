# Circles fade out
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

# 1: Declare and 2: initialize the variable!
circle1_x = 0
circle1_y = 0
circle2_x = 0
circle2_y = 0
circle3_x = 0
circle3_y = 0
circle_size = 0
circle_color = 0
bright1 = 0  # brightness value
bright2 = 0  # brightness value
bright3 = 0  # brightness value

def setup():
    global circle1_x, circle1_y, circle2_x, circle2_y, circle3_x, circle3_y, circle_size
    size(640, 360)
    circle_size = 100  # circle size

    circle1_x = 320
    circle1_y = 90

    circle2_x = 120
    circle2_y = 160

    circle3_x = 550
    circle3_y = 220
    background(45, 197, 244)

def draw():
    global bright1, bright2, bright3
    background(45, 197, 244)

    no_stroke()

    # Use the variables!
    fill(bright1)  # circle color/brightness
    circle(circle1_x, circle1_y, circle_size)

    fill(bright2)
    circle(circle2_x, circle2_y, circle_size)

    fill(bright3)
    circle(circle3_x, circle3_y, circle_size)

    # increase brightness values
    bright1 = bright1 + 8
    bright2 = bright2 + 4
    bright3 = bright3 + 3

run()
