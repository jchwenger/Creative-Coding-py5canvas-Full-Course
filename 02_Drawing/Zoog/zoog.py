# Translated to py5canvas

from py5canvas import *

def setup():
    size(480, 270)
    rect_mode(CENTER)
    color_mode("rgb", 255, 255, 255, 100)
    background(100, 0, 150)

def draw():

    # Legs
    stroke(255, 255, 0)
    stroke_weight(8)
    line(235, 180, 220, 205)
    line(245, 180, 260, 205)

    # Body
    no_stroke()
    fill(255, 150, 200, 75)
    rect(240, 145, 25, 100)

    # Head
    fill(255, 200, 100)
    circle(240, 115, 60)

    # Eyes
    fill(0, 150, 255)
    ellipse(221, 115, 16, 32)
    ellipse(259, 115, 16, 32)

run()
