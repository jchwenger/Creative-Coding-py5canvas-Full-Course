# Concentric circles
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

def setup():
    size(640, 360)

def draw():
    background(0)
    no_fill()
    stroke(255)
    stroke_weight(2)

    for radius in range(10, 150, 10):
        circle(width/2, height/2, radius*2)

run()
