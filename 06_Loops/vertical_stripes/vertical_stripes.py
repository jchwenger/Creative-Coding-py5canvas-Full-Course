# Vertical Stripes
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

w = 20

def setup():
    size(640, 360)

def draw():
    background(0)
    fill(255)
    no_stroke()
    for x in range(0, int(width), int(w * 2)):
        rect(x, 0, w, height)

run()
