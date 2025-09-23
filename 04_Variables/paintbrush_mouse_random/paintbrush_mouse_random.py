# Paintbrush: random color when mouse pressed
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

r = 0
g = 0
b = 0

def setup():
    global r, g, b
    size(640, 320)
    background(255)

    r = 255
    g = 250
    b = 150

def draw():
    global r, g, b
    fill(r, g, b)
    no_stroke()
    circle(mouse_x, mouse_y, 24)

def mouse_pressed():
    global r, g, b
    # background(255)
    r = random(255)
    g = random(255)
    b = random(255)

run()
