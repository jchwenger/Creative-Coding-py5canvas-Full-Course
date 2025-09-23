from py5canvas import *

# Two bubble classes (with pop animation)
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

# TODO: fix imports
class Bubble:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.initial_size = r
        self.grow_rate = random(0.1, 0.3)
        self.acceleration = random(0.0005, 0.01)
        self.should_pop = False
        self.animation_count = 0
        self.bub_col = color(random(100, 255), 0, random(100, 255), 200)

    def update(self):
        self.y = self.y - random(1, 4)
        self.x = self.x + random(-1, 1)
        self.r = self.r + self.grow_rate
        self.grow_rate += self.acceleration

    def show(self):
        self.should_pop = self.check_size()
        duration = 0.1
        if self.should_pop:
            self.animate_pop()
            self.reset_pop(duration)
        else:
            stroke_weight(2)
            stroke(255)
            fill(self.bub_col)
            circle(self.x, self.y, self.r * 2)
            stroke_weight(self.r / 5)
            arc(self.x, self.y, self.r, self.r, PI, radians(250))

    def animate_pop(self):
        stroke_weight(10)
        stroke(255)
        num_lines = 5
        line_length = 20
        angle = 0
        while angle < TWO_PI:
            x1 = self.x + self.r * cos(angle)
            y1 = self.y + self.r * sin(angle)
            x2 = self.x + (self.r + line_length) * cos(angle)
            y2 = self.y + (self.r + line_length) * sin(angle)
            line(x1, y1, x2, y2)
            text_size(24)
            text_align(CENTER, CENTER)
            fill(255)
            text("POP", self.x, self.y)
            angle += TWO_PI / num_lines
        self.animation_count += 1

    def edges(self):
        if self.y < -self.r:
            self.y = height + self.r / 2

    def reset_pop(self, duration):
        if self.animation_count > duration * 60:
            self.y = height + self.r / 2
            self.should_pop = False
            self.r = self.initial_size
            self.animation_count = 0
            self.grow_rate = 0
            self.acceleration = random(0.0005, 0.02)

    def check_size(self):
        return self.r > self.initial_size * 2


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

    # show and update raindrops
    for drop in drops:
        drop.update()
        drop.edges()
        drop.show()


run()
