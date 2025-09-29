# Fruit Data Visualization
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

fruit_inventory = [0.0] * 5
fruit_names = ["mango", "strawberry", "kiwi", "plum", "blueberry"]

# Another way to represent colors instead of RGB, is by using
# hexidecimal notation (ex: #FFFFFF is the color white). Many
# color palettes found online use hex codes to denote colors.
# You can convert RGB to Hex or vice versa using online tools.
# TODO: Hex color support - not implemented in py5canvas yet
# color_array = [#D9A407, #EE0E00, #8C6432, #9253A1, #4188FF]
color_array = [color(217, 164, 7), color(238, 14, 0), color(140, 100, 50), color(146, 83, 161), color(65, 136, 255)]

def setup():
    global fruit_inventory
    size(640, 360)

    for i in range(len(fruit_inventory)):
        fruit_inventory[i] = random(25, 145)


def mouse_pressed():
    global fruit_inventory
    # randomize when mouse pressed
    for i in range(len(fruit_inventory)):
        fruit_inventory[i] = random(25, 145)

def draw():
    background(0, 0, 50)
    stroke_cap(SQUARE)
    text_align(CENTER)
    text_size(24)

    for i in range(len(fruit_inventory)):
        rect_mode(CORNER)
        stroke_weight(2)
        stroke(color_array[i])
        no_fill()

        x = 80 + i * 120

        # bar outline
        rect(x - 12, height/2, 24, -150)

        # line height is number of fruit inventory
        stroke_weight(24)
        line(x, height/2, x, height/2 - fruit_inventory[i])

        fill(color_array[i])
        no_stroke()
        text(fruit_names[i], x, height/2 + 24)  # fruit name labels

        # We declared the fruit inventory array as having floats
        # which means the random values we assign will be decimal
        # numbers, but if you want to display a whole number you can use
        # int() to convert a float to an integer. See what happens
        # when you remove int()!
        text("qty: " + str(int(fruit_inventory[i])), x, height/2 + 48)  # display number of each fruit

    fill(240)
    text_size(14)
    no_stroke()
    stroke_weight(1)

    text_align(LEFT, CENTER)
    text("FRUIT INVENTORY", 40, height - 40)

    text_align(CENTER, CENTER)
    text("CTRL + ALT + DELI", width/2, height - 40)

    text_align(RIGHT, CENTER)
    text("EST. 2001", width - 40, height - 40)

run()
