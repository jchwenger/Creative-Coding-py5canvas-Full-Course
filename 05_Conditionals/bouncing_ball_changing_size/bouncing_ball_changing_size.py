# Bouncing ball changing size
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

x = 0
y = 0
xspeed = 0
yspeed = 0
radius = 0
rspeed = 0

def setup():
    global x, y, xspeed, yspeed, radius, rspeed
    size(640, 360)
    xspeed = 2
    yspeed = 2
    rspeed = 0.50  # speed at which radius changes
    radius = 25

    # Start at a random location!
    x = random(radius, width-radius)
    y = random(radius, height-radius)

def draw():
    global x, y, radius, xspeed, yspeed, rspeed
    background(0)
    no_stroke()
    fill(255)

    min_size = 10
    max_size = 100

    # Check if ball bounces on edges!
    if x < radius or x > width - radius:
        xspeed = xspeed * -1
        rspeed = rspeed * -1

    if y < radius or y > height - radius:
        yspeed = yspeed * -1
        rspeed = rspeed * -1

    circle(x, y, radius*2)

    x = x + xspeed
    y = y + yspeed
    # The constrain function constrains a value to not exceed a minimum and maximum value.
    radius = constrain(radius + rspeed, min_size, max_size)

run()
