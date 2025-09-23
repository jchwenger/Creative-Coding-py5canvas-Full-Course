# Color Palette Array
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

# Another way to represent colors instead of RGB, is by using
# hexidecimal notation (ex: #FFFFFF is the color white). Many
# color palettes found online use hex codes to denote colors.
# You can convert RGB to Hex or vice versa using online tools.
# color_array = []{#0b6a88, #ec015a, #f89e4f, #2dc5f4, #9253a1};
# Color using RGB
color_array = [color(11, 106, 136), color(236, 1, 90), color(248, 158, 79), color(45, 197, 244), color(146, 83, 161)]

def setup():
    size(640, 360)
    rect_mode(CENTER)

def draw():
    background(255)
    no_stroke()

    size_val = 100
    for i in range(len(color_array)):
        fill(color_array[i])  # fill with the colors in the array

        # place the rectangles so they are centered based on the amount of colors/shapes
        initial_x = width/2 - size_val*len(color_array)/2 + size_val/2
        rect(initial_x + size_val*i, height/2, size_val, size_val*2)

        # labels
        fill(240)
        text_size(18)
        text_align(LEFT, CENTER)

        # convert the red value of each color to an integer
        # TODO: red(), green(), blue() functions - not implemented in py5canvas yet
        # r = int(red(color_array[i]))
        # g = int(green(color_array[i]))
        # b = int(blue(color_array[i]))

        r = int(color_array[i][0])
        g = int(color_array[i][1])
        b = int(color_array[i][2])

        text("r: " + str(r), size_val+size_val*i - 20, 60 + height/2 - 18)
        text("g: " + str(g), size_val+size_val*i - 20, 60 + height/2)
        text("b: " + str(b), size_val+size_val*i - 20, 60 + height/2 + 20)

    fill(0)
    text_size(14)
    text("PALETTE NAME: THE CODING RAINBOW", size_val - 30, height/2 + size_val + 10)

run()
