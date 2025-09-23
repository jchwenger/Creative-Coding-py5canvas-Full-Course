# Paintbrush: random color/random size
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

def setup():
    size(640, 320)
    background(255)

def draw():
    rand_red = random(255)
    rand_blue = random(50, 150)
    rand_green = random(150, 255)

    fill(rand_red, rand_blue, rand_green)
    no_stroke()
    circle(mouse_x, mouse_y, random(10, 50))

def mouse_pressed():
    background(255)

run()
