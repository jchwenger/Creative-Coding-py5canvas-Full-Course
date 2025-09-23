# Circle - move y only
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

# 1: Declare and 2: initialize the variable!
circle_x = 0
circle_y = 0
circle_size = 0

def setup():
    global circle_x, circle_y, circle_size
    size(640, 360)
    circle_size = 48
    circle_x = width/2
    circle_y = 3*height/4
    background(0)

def mouse_pressed():
    global circle_y
    # reset when mouse is pressed!
    circle_y = 3*height/4

def draw():
    global circle_x, circle_y
    background(0)

    # Use the variables!
    no_stroke()
    fill(255)
    circle(circle_x, circle_y, circle_size)

    # 1: Gradually move circle up
    circle_y = circle_y - 1

run()
