from py5canvas import *
import random as rnd

# Flower class
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

# Change from original: accepts an optional palette
class Flower:
    def __init__(self, x, y, palette=None):
        self.x = x
        self.y = y
        # unlike in the original, for now we can't have a size-zero flower
        self.size = 1
        self.max_size = 50
        # pick a random color from provided palette or a default
        if palette is None:
            palette = [
                color(154, 86, 255),
                color(82, 122, 242),
                color(242, 184, 7),
                color(242, 137, 7),
                color(242, 34, 15),
            ]
        # using random.choice to select one from the list
        self.fill_col = rnd.choice(palette)
        self.wink_counter = 0

    def show_flower(self):
        self._petals()
        self._show_face()

    def update(self):
        # oscillate the size of the flower
        self.size = 200 + 100 * cos(radians(frame_count))
        self.wink_counter += 1
        if self.wink_counter > 360:
            self.wink_counter = 0

    def _petals(self):
        # make the petals with thick lines
        stroke_weight(self.size / 2)
        stroke(self.fill_col)
        petal_size = self.size / 3
        line(self.x - petal_size, self.y - petal_size, self.x + petal_size, self.y + petal_size)
        line(self.x + petal_size, self.y - petal_size, self.x - petal_size, self.y + petal_size)
        line(self.x + self.size / 2, self.y, self.x - self.size / 2, self.y)
        line(self.x, self.y + self.size / 2, self.x, self.y - self.size / 2)

        # flower center
        no_stroke()
        # decrease the brightness of the main color for the center of the flower
        fill(self.fill_col[0], self.fill_col[1], self.fill_col[2] - 100)
        circle(self.x, self.y, self.size)

    def _show_face(self):
        # face
        fill(255)
        stroke(255)
        stroke_weight(self.size / 35)
        if self.wink_counter < 10:
            line(self.x - self.size / 4 - self.size / 20, self.y, self.x - self.size / 4 + self.size / 20, self.y)
        else:
            circle(self.x - self.size / 4, self.y, self.size / 10)
        circle(self.x + self.size / 4, self.y, self.size / 10)
        no_fill()
        arc(self.x, self.y + self.size / 10, self.size / 5, self.size / 5, 0, PI)

# Define a rainbow palette similar to the PDE for consistency
rainbow_colors = [
    color(154, 86, 255),
    color(82, 122, 242),
    color(242, 184, 7),
    color(242, 137, 7),
    color(242, 34, 15),
]

# Global
f = None


def setup():
    global f
    size(640, 360)

    # Use HSB with 0..255 ranges as in PDE
    color_mode(HSB, 255)

    f = Flower(width / 2, height / 2, palette=rainbow_colors)


def draw():
    background(150, 30, 255)
    f.show_flower()
    f.update()


run()
