# Bubble class
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

class Bubble:
    def __init__(self):
        self.x = random(width)
        self.y = height
        self.r = random(32, 128)
        self.bub_col = color(random(100, 255), random(100, 200), 255)  # bubble color

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
    bub0 = Bubble()
    bub1 = Bubble()

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
