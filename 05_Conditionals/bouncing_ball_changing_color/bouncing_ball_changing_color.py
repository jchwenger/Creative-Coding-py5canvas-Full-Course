# Bouncing ball changing color
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

x = 0
y = 0
xspeed = 0
yspeed = 0
radius = 0

def setup():
    global x, y, xspeed, yspeed, radius
    size(640, 360)
    xspeed = 2
    yspeed = 2
    radius = 25

    # Start at a random location!
    x = random(radius, width-radius)
    y = random(radius, height-radius)

def draw():
    global x, y, xspeed, yspeed
    background(0)
    no_stroke()

    # If ball touches an edge, change the color!
    if x < radius or x > width - radius:
        xspeed = xspeed * -1
        fill(random(255), random(255), random(255))

    if y < radius or y > height - radius:
        yspeed = yspeed * -1
        fill(random(255), random(255), random(255))

    circle(x, y, radius*2)

    x = x + xspeed
    y = y + yspeed

run()
