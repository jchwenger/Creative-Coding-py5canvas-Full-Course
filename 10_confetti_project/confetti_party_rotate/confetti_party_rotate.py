# Confetti Party!!! with rotate
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

import random as rnd
from py5canvas import *

# Another way to represent colors instead of RGB, is by using
# hexidecimal notation (ex: #FFFFFF is the color white). Many
# color palettes found online use hex codes to denote colors.
# You can convert RGB to Hex or vice versa using online tools.
# Hex color support, yay!, implemented in py5canvas!
rainbow_colors = ["#9A56FF", "#527AF2", "#F2B807", "#F28907", "#F2220F"]


class Confetti:
    def __init__(self):
        self.x = -1000
        self.y = -1000
        self.w = 8 # confetti width
        self.h = random(4, 12) # confetti height
        self.xspeed = 0
        self.yspeed = 0
        self.angle = 0
        self.angle_speed = random(-0.1, 0.1)
        self.color = rnd.choice(rainbow_colors)

    def burst(self, mx, my):
        self.x = mx
        self.y = my
        self.xspeed = random(-5, 5)
        self.yspeed = random(-5, 5)

    def update(self):
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed

        self.yspeed = self.yspeed + 0.1
        self.angle = self.angle + self.angle_speed

    def show(self):
        push()
        translate(self.x, self.y)
        rotate(self.angle)
        fill(self.color)
        no_stroke()
        rect_mode(CENTER)
        rect(0, 0, self.w, self.h)
        pop()


# Global variables
# (unlike in Java, the most-used container, List, already
# behaves like an ArrayList (resizeable)
confetti = []
party_time = False


def setup():
    global confetti
    size(640, 360)

    for i in range(100):
        confetti.append(Confetti())


def mouse_pressed():
    global party_time
    party_time = True
    for c in confetti:
        c.burst(mouse_x, mouse_y)


def draw():
    background(255)
    if party_time:
        for c in confetti:
            c.show()
            c.update()


run()
