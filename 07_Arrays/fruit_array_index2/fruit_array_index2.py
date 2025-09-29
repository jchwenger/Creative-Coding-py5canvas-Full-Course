# Fruit array 2 - parse the array forward & backward
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

fruit_inventory = [50, 100, 70, 110]
fruit_names = ["mango", "strawberry", "kiwi", "plum"]
index = 0
go_forward = True

def setup():
    size(640, 360)

def mouse_pressed():
    global index, go_forward
    # go through the array forward and backward

    if go_forward:
        # go forward
        index = index + 1
    else:
        # go backward
        index = index - 1

    if index >= len(fruit_inventory)-1 or index <= 0:
        go_forward = not go_forward  # reverse the direction

def draw():
    background(0)
    stroke(255)
    stroke_weight(24)
    stroke_cap(SQUARE)

    # line height is number of fruit inventory
    line(width/2, height/2, width/2, height/2 - fruit_inventory[index])

    text_align(CENTER)
    no_stroke()
    text_size(64)
    fill(255)
    text(fruit_names[index], width/2, height/2 + 64)

    # Using '+' lets you add (concatenate) strings or strings and variables
    text("index = " + str(index), width/2, height/2 + 64*2)

run()
