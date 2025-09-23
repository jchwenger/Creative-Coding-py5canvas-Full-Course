# Horizontal Stripes
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

h = 20

def setup():
    size(640, 360)

def draw():
    background(0)
    fill(255)
    no_stroke()
    for y in range(0, int(height), int(h * 2)):
        rect(0, y, width, h)

run()
