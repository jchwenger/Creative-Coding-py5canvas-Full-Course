# Self Portrait
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *



def setup():
    size(640, 360)  # canvas size
    background(255)  # set background color
    rect_mode(CENTER)

def draw():
    # body
    rect(320, 180 + 125, 160, 150)
    triangle(320 - 80, 180 + 50, 320, 360, 320 + 80, 180+50)

    # head
    circle(320, 180, 150)

    # eyes
    circle(320 - 30, 180 - 15, 25)
    square(320 + 30, 180 - 15, 30)

    # eyebrows
    rect(320 - 30, 180 - 25, 50, 10)
    rect(320 + 30, 180 - 45, 50, 10)

    # mouth
    arc(320, 180+25, 50, 50, 0, PI, CLOSE)

run()
