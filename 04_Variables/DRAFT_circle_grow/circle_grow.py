# Circle growing
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
    circle_size = 0  # initial circle size
    circle_x = width/2
    circle_y = 3*height/4
    background(45, 197, 244)

def draw():
    global circle_x, circle_y, circle_size
    no_stroke()
    fill(255, 255, 0)  # circle color

    # Use the variables!
    circle(circle_x, circle_y, circle_size)

    # 1: Gradually move circle up while 2: circle increases in size
    circle_y = circle_y - 1
    circle_size = circle_size + 1

    # Add a candle stick!
    rect_mode(CENTER)
    fill(240)

    rect(width/2, height, 15, height/2)

    # TODO: Implement 5th parameter in rect rounds the corners.
    # Check out the reference page for more detail!
    # rect(width/2, height, 15, height/2, 5)

run()
