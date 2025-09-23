# Flower
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

def setup():
    size(640, 360)  # canvas size
    background(0)  # set background color

    stroke(0)  # black outline
    rect(320-5, 180, 10, 320)

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

    stroke(0)  # black outline
    circle(320, 180, 85)  # flower center

run()
