# Confetti Party!!!
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

class Confetti:
    def __init__(self):
        self.x = -1000
        self.y = -1000
        self.xspeed = 0
        self.yspeed = 0

    def burst(self, mx, my):
        self.x = mx
        self.y = my
        self.xspeed = random(-5, 5)
        self.yspeed = random(-5, 5)

    def update(self):
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
        self.yspeed = self.yspeed + 0.1

    def show(self):
        fill(0)
        rect_mode(CENTER)
        square(self.x, self.y, 10)

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
