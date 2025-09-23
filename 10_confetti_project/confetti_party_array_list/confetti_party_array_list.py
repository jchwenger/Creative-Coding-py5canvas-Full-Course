# Add elements using ArrayList
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

import random as rnd
from py5canvas import *

# Another way to represent colors instead of RGB, is by using
# hexidecimal notation (ex: #FFFFFF is the color white). Many
# color palettes found online use hex codes to denote colors.
# You can convert RGB to Hex or vice versa using online tools.
# TODO: Hex color support - not implemented in py5canvas yet
# rainbow_colors = [#9A56FF, #527AF2, #F2B807, #F28907, #F2220F]
rainbow_colors = [color(154, 86, 255), color(82, 122, 242), color(242, 184, 7), color(242, 137, 7), color(242, 34, 15)]


# TODO: fix imports
class Confetti:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.w = 8; # confetti width
        self.h = random(4, 12); # confetti height
        self.xspeed = random(-5, 5)
        self.yspeed = random(-5, 5)
        self.angle = 0
        self.angle_speed = random(-0.1, 0.1)
        # TODO: implement random(1D-array)? https://p5js.org/reference/p5/random/
        # or handle conflict with `import random` in Python?
        self.color = rnd.choice(rainbow_colors)

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
clusters = []  # create ArrayList equivalent
party_time = False


def setup():
    size(640, 360)


def mouse_pressed():
    global party_time
    party_time = True

    # each time the mouse is pressed, add 100 more confetti
    for i in range(100):
        clusters.append(Confetti(mouse_x, mouse_y))


def draw():
    background(255)
    if party_time:
        for c in clusters:
            c.show()
            c.update()


run()
