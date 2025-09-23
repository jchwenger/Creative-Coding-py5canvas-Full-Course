# Random Lines
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

x1 = 0
y1 = 0
x2 = 0
y2 = 0

def setup():
    size(640, 360)
    background(0)

def draw():
    global x1, y1, x2, y2
    stroke(random(150, 255), random(100, 250), 0, 200)
    stroke_weight(random(1, 4))
    x1 = random(width)
    y1 = random(height)
    x2 = x1 + random(-50, 50)
    y2 = y1 + random(-50, 50)
    line(x1, y1, x2, y2)

run()
