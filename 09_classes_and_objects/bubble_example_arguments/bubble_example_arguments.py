# Two bubbles
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

class Bubble:
    def __init__(self, x, r):
        self.x = x
        self.y = 360
        self.r = r
        self.bub_col = color(255, 192, 203)  # bubble color

    def update(self):
        self.y = self.y - random(1, 4)
        self.x = self.x + random(-1, 1)

    def show(self):
        stroke_weight(4)
        fill(self.bub_col)
        circle(self.x, self.y, self.r*2)

    def edges(self):
        # place bubble back at the bottom of canvas
        if self.y < -self.r:
            self.y = height + self.r/2

# Global variables
bub0 = None
bub1 = None  # add second bubble

def setup():
    global bub0, bub1
    size(640, 360)

    # initialize bubbles
    bub0 = Bubble(100, 10)
    bub1 = Bubble(500, 100)

def draw():
    background(255)

    # show and update bubbles
    bub0.update()
    bub0.edges()
    bub0.show()

    bub1.update()
    bub1.edges()
    bub1.show()

run()
