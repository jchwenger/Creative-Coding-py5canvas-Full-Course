# Flower
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

def setup():
    size(640, 360)  # canvas size
    background(255)  # set background color

def draw():
    stroke(0, 128, 0)  # stem color
    stroke_weight(10)  # thickness of line
    line(320, 180, 320, 360)  # stem

    fill(147, 112, 219)  # petal color
    no_stroke()  # no circle outline

    # petals
    circle(320 + 50, 180, 50)
    circle(320 - 50, 180, 50)
    circle(320, 180 + 50, 50)
    circle(320, 180 - 50, 50)
    circle(320 - 37.5, 180 - 37.5, 50)
    circle(320 + 37.5, 180 + 37.5, 50)
    circle(320 - 37.5, 180 + 37.5, 50)
    circle(320 + 37.5, 180 - 37.5, 50)

    fill(255, 255, 0)  # flower center color
    circle(320, 180, 85)  # flower center

run()
