# Translated to py5canvas

from py5canvas import *

def setup():
    size(640, 360)
    background(255, 0, 150)

def draw():
    no_stroke()
    fill(99, 50, 200)
    circle(500, 180, 150)

    stroke_weight(4)
    stroke(100, 150, 200, 255)
    no_fill()
    rect_mode(CENTER)
    square(400, 180, 100)

run()
