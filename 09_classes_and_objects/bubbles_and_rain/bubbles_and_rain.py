from py5canvas import *

# Two bubble classes
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas


# TODO: fix imports
class Bubble:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.bub_col = color(random(100, 255), 0, random(100, 255), 200)

    def update(self):
        self.y = self.y - random(1, 4)
        self.x = self.x + random(-1, 1)

    def show(self):
        stroke_weight(2)
        stroke(255)
        fill(self.bub_col)
        circle(self.x, self.y, self.r * 2)
        stroke_weight(self.r / 5)
        arc(self.x, self.y, self.r, self.r, PI, radians(250))

    def edges(self):
        if self.y < -self.r:
            self.y = height + self.r / 2

class RainDrop:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.yspeed = 0
        self.r = 10
        self.drop_color = color(0, 0, 255)

    def update(self):
        self.y = self.y + self.yspeed
        self.yspeed += 0.1

    def show(self):
        no_stroke()
        fill(self.drop_color)
        for i in range(1, 10):
            circle(self.x, self.y - i, self.r - i)

    def edges(self):
        if self.y > height + self.r:
            self.y = -height
            self.yspeed = 0

# Global variables
bubbles = []
drops = []


def setup():
    global bubbles, drops
    size(640, 360)

    # initialize big bubbles
    for i in range(5):
        x = random(width)
        y = random(height)
        r = random(20, 40)
        bubbles.append(Bubble(x, y, r))

    # initialize raindrops
    for j in range(100):
        x = random(width)
        y = random(-height, height)
        drops.append(RainDrop(x, y))


def draw():
    background(200, 200, 255)

    # show and update bubbles
    for bubble in bubbles:
        bubble.update()
        bubble.edges()
        bubble.show()

    for drop in drops:
        drop.update()
        drop.edges()
        drop.show()


run()
