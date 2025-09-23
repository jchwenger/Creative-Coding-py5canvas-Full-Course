# Bouncing ball with gravity
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

x = 0
y = 0
radius = 0
vel_y = 0  # velocity
acc_y = 0  # acceleration

def setup():
    global x, y, radius, vel_y, acc_y
    size(640, 360)
    radius = 25

    vel_y = 3  # initial velocity
    acc_y = 1  # acceleration/gravity

    # position of ball
    x = width/2
    y = height/4

def draw():
    global y, vel_y
    background(0)
    no_stroke()

    vel_y = vel_y + acc_y
    y = y + vel_y

    if y < radius or y > height - radius:
        vel_y = vel_y * -.85  # reduce the speed each time ball hits floor
        y = height - radius


    circle(x, y, radius*2)

run()
