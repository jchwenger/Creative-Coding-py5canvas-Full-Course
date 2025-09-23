# Bouncing ball changing speed
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

x = 0
y = 0
xspeed = 0
yspeed = 0
radius = 0
max_speed = 10

def setup():
    global x, y, xspeed, yspeed, radius
    size(640, 360)
    xspeed = 5
    yspeed = 5
    radius = 25

    # Start at a random location!
    x = random(radius, width-radius)
    y = random(radius, height-radius)

def draw():
    global x, y, xspeed, yspeed
    background(0)
    no_stroke()

    if x < radius or x > width - radius:
        xspeed = constrain(random(xspeed, xspeed*2), -max_speed, max_speed) * -1

        # abs() returns the absolute value
        if abs(xspeed) == max_speed:
            xspeed = xspeed/5  # reset

    if y < radius or y > height - radius:
        yspeed = constrain(random(yspeed, yspeed*2), -max_speed, max_speed) * -1

        # abs() returns the absolute value
        if abs(yspeed) == max_speed:
            yspeed = yspeed/5  # reset

    circle(x, y, radius*2)

    x = x + xspeed
    y = y + yspeed

run()
