# Paintbrush with conditional
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

min_size = 10
max_size = 100
circle_size = min_size  # circle starts at min size
speed = 1  # speed of size changing

def setup():
    global circle_size
    size(640, 360)
    background(240)

def draw():
    global circle_size
    circle(mouse_x, mouse_y, circle_size)
    stroke(240, 80)
    fill(236, 1, 90)

    # reset to minimum size once size > maxSize
    if circle_size >= max_size:
        circle_size = min_size

    if circle_size >= max_size/2:
        fill(112, 50, 126)

    circle_size = circle_size + speed  # change the size of the circle

def mouse_pressed():
    background(240)

run()
