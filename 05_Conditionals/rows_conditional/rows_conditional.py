# Rows conditional example
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

def setup():
    size(640, 360)

def draw():
    background(0)
    stroke(255)
    fill(175)
    rect_mode(CENTER)

    # Check the mouseY position to determine what's displayed!
    if mouse_y < 120:
        line(250, 130, 350, 220)
    elif mouse_y < 240:
        square(300, 180, 100)
    else:
        circle(300, 180, 100)

    stroke(127)
    stroke_weight(4)

    # Draw horizontal lines
    line(0, 120, width, 120)
    line(0, 240, width, 240)

run()
