# Ball turning around
# Translated to py5canvas

from py5canvas import *

x = 0
speed = 4

def setup():
    size(640, 360)

def draw():
    global x, speed
    background(0)
    no_stroke()
    fill(255)

    circle(x, height/2, 48)

    x = x + speed

    if x > width:
        speed = -4

run()
