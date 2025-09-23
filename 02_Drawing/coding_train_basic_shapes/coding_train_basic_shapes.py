# Basic shapes
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

def setup():
    size(640, 360)
    
    background(200)

    circle(500, 180, 100)

    rect_mode(CENTER)
    square(100, 180, 100)

    line(100, 180, 500, 180)

run()
