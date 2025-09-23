# Variables example using mouseX, mouseY, width, height
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

def setup():
    size(640, 320)

def draw():
    background(255)
    line(mouse_x, 0, mouse_x, height)  # vertical line
    line(0, mouse_y, width, mouse_y)  # horizontal line

run()
