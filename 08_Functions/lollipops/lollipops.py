# Lollipops
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

# Another way to represent colors instead of "rgb", is by using
# hexidecimal notation (ex: #FFFFFF is the color white). Many
# color palettes found online use hex codes to denote colors.
# You can convert "rgb" to Hex or vice versa using online tools.
# Hex color support, yay!, implemented in py5canvas!
rainbow_colors = ["#9A56FF", "#527AF2", "#F2B807", "#F28907", "#F2220F"]

def setup():
    size(640, 360)

    # TODO: Not currently working, see TODO.md
    # Use hue, saturation and brightness to specify
    # color with a minimum value of 0 and maximum value of
    # 255.
    # color_mode("hsb", 255)

def draw():
    background(150, 30, 255)

    sunshine()
    cloud(110, 75, 100)
    cloud(450, 95, 50)
    lollipop(100, 180, 100, rainbow_colors[0])
    lollipop(210, 180, 150, rainbow_colors[1])
    lollipop(320, 180, 70, rainbow_colors[2])
    lollipop(430, 180, 120, rainbow_colors[3])
    lollipop(540, 180, 80, rainbow_colors[4])

def lollipop(x, y, size, fill_col):
    # stem
    stroke_weight(1)
    fill(255)
    no_stroke()
    rect(x - 5, y, 10, height - y - 20)

    # lollipop
    no_stroke()
    fill(fill_col)
    circle(x, y, size)
    rect_size = size + 10  # lollipop center shape

    rect(x - rect_size/2, y - rect_size/8, rect_size, rect_size/4)

    rect(x - rect_size/2, y - rect_size/8, rect_size, rect_size/4, 5)

    stroke(fill_col[1], fill_col[0] - 100, fill_col[0])  # highlight
    line(x - rect_size/2 + rect_size/8, y - rect_size/8, x + rect_size/2 - rect_size/8, y - rect_size/8)
    stroke(fill_col[0], fill_col[0], fill_col[0] - 100)  # shadow
    line(x - rect_size/2 + rect_size/8, y + rect_size/8, x + rect_size/2 - rect_size/8, y + rect_size/8)

    # white arc for glossy effect
    no_fill()
    stroke_weight(5)
    stroke(255, 0, 255)
    arc(x, y, size - 20, size - 20, PI, PI + PI/3)

def sunshine():
    no_stroke()
    fill(35, 255, 255)
    circle(60, 60, 100)

def cloud(pos_x, pos_y, size):
    for i in range(3):
        fill(255, 0, 255)
        no_stroke()
        circle(pos_x + size/2*i, pos_y, size)

run()
