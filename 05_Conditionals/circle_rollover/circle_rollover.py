# Circle rollover
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

xpos = 0
ypos = 0
radius = 0

def setup():
    global xpos, ypos, radius
    size(640, 360)
    xpos = width/2
    ypos = height/2
    radius = 100

def draw():
    background(0)
    stroke(255)
    stroke_weight(4)

    # Check the distance of the mouse from center of circle
    distance = dist(mouse_x, mouse_y, xpos, ypos)

    # If mouse is within circle, fill white
    if distance < radius:
        fill(255)
    else:
        fill(175)

    circle(xpos, ypos, radius*2)

run()
