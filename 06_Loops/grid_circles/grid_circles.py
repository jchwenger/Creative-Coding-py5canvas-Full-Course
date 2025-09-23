# Grid of circles
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

spacing = 40

def setup():
    size(640, 360)

def draw():
    background(0)
    fill(255)
    no_stroke()

    for x in range(0, int(width) + 1, int(spacing)):
        for y in range(0, int(height) + 1, int(spacing)):
            circle(x + spacing/2, y + spacing/2, spacing)

run()
