# Bubble Mouse Interaction
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

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

    def within_bubble(self, mouse_x, mouse_y):
        distance = dist(mouse_x, mouse_y, self.x, self.y)
        return distance < self.r

    def change_color(self):
        self.bub_col = color(random(100, 255), 0, random(100, 255), 200)

# Global variables
bubbles = []


def setup():
    global bubbles
    size(640, 360)

    # initialize big bubbles
    for i in range(5):
        x = random(width)
        y = random(height)
        r = random(20, 40)
        bubbles.append(Bubble(x, y, r))


def draw():
    background(200, 200, 255)

    # show and update bubbles
    for bubble in bubbles:
        bubble.update()
        bubble.edges()
        bubble.show()


def mouse_pressed():
    # check each bubble to verify if mouse is over any bubble
    for bubble in bubbles:
        in_bubble = bubble.within_bubble(mouse_x, mouse_y)
        if in_bubble:
            bubble.change_color()


run()
