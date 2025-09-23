# Paintbrush: plain
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

def setup():
    size(640, 320)
    background(255)

def draw():
    no_stroke()
    fill(0)
    circle(mouse_x, mouse_y, 24)

run()
