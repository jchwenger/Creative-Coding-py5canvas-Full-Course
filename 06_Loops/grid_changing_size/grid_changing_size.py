# Grid changing resolution
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

spacing = 30
max_spacing = 0
min_spacing = 0
theta = 0

def setup():
    global max_spacing, min_spacing
    size(640, 360)
    max_spacing = 80
    min_spacing = 30

def draw():
    global spacing, theta
    background(0)
    fill(255)
    stroke_weight(2)

    for x in range(0, int(width) + 1, int(spacing)):
        for y in range(0, int(height) + 1, int(spacing)):
            rect(x, y, spacing, spacing)

    # the sin or cosine function help create oscillating motion
    theta += radians(1)
    spacing = max_spacing*(1+sin(theta)) + min_spacing

run()
