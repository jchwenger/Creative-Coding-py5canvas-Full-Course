# Abstract
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

def setup():
    size(640, 360)  # canvas size
    background(255)  # set background color
    no_fill()  # don't fill the shapes
    stroke_weight(50)  # line thickness

def draw():
    line(0, 120, 500, 400)
    circle(300, 150, 200)
    rect_mode(CENTER)
    square(515, 240, 200)

run()
