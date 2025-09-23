# Lollipops
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

# Another way to represent colors instead of "rgb", is by using
# hexidecimal notation (ex: #FFFFFF is the color white). Many
# color palettes found online use hex codes to denote colors.
# You can convert "rgb" to Hex or vice versa using online tools.
# TODO: Hex color support - not implemented in py5canvas yet
# rainbow_colors = [#9A56FF, #527AF2, #F2B807, #F28907, #F2220F]
rainbow_colors = [color(154, 86, 255), color(82, 122, 242), color(242, 184, 7), color(242, 137, 7), color(242, 34, 15)]

def setup():
    size(640, 360)

    # Use hue, saturation and brightness to specify
    # color with a minimum value of 0 and maximum value of
    # 255.
    color_mode("hsb", 255)

def draw():
    background(150, 30, 255)

    sunshine()
    cloud(110, 75, 100)
    cloud(450, 95, 50)

    for i in range(len(rainbow_colors)):
        fill_col = rainbow_colors[i]  # color of lollipop
        size = 100  # size of lollipop
        pos_x = size/2 + 15 + (width/len(rainbow_colors))*i  # x position

        # Start each lollipop at a different point in the sine function by offsetting the phase.
        # When removing phase in the sine function below, all lollipops move in unison
        phase = PI/len(rainbow_colors) * i

        # frameCount contains the number of frames displayed since the program started.
        # It can be used with an oscillating function like sine or cosine, which returns a
        # number between -1 and 1. Try multiplying frameCount by a number.
        # TODO: frameCount - not implemented in py5canvas yet, using millis()/16.67 as approximation
        oscillate = ease_in(abs(sin(radians(millis()/16.67) + phase)))
        pos_y = height/2 + 50 - 100*oscillate  # y position

        lollipop(pos_x, pos_y, size, fill_col, oscillate)

def ease_in(num):
    # "Easing functions specify the rate of change of a parameter over time.
    # Objects in real life don't just start and stop instantly, and almost
    # never move at a constant speed." Reference the following resource for
    # more information about different easing functions: https://easings.net

    # num should be a number between 0 and 1.

    easing = 0
    if num < 0.5:
        easing = (1 - np.sqrt(1 - pow(2 * num, 2))) / 2
    else:
        easing = (np.sqrt(1 - pow(-2 * num + 2, 2)) + 1) / 2

    return easing

def lollipop(x, y, size, fill_col, oscillate):
    # shadow
    fill(0, 20)
    no_stroke()

    # use the oscillation to vary the size of the shadow. The closer the lollipop
    # is to the ground, the bigger the shadow gets
    ellipse(x, height - 20, (size*(1-oscillate)), (size*(1-oscillate)/2))

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
    # rect(x - rect_size/2, y - rect_size/8, rect_size, rect_size/4, 5)

    # TODO: hue(), saturation(), brightness() functions - not implemented in py5canvas yet
    # stroke(hue(fill_col), saturation(fill_col) - 100, brightness(fill_col))  # highlight
    # line(x - rect_size/2 + rect_size/8, y - rect_size/8, x + rect_size/2 - rect_size/8, y - rect_size/8)
    # stroke(hue(fill_col), saturation(fill_col), brightness(fill_col) - 100)  # shadow
    # line(x - rect_size/2 + rect_size/8, y + rect_size/8, x + rect_size/2 - rect_size/8, y + rect_size/8)

    # white arc for glossy effect
    no_fill()
    stroke_weight(5)
    stroke(255)
    arc(x, y, size - 20, size - 20, PI, PI + PI/3)

def sunshine():
    no_stroke()
    fill(35, 255, 255)
    circle(60, 60, 100)

def cloud(pos_x, pos_y, size):
    for i in range(3):
        fill(255)
        no_stroke()
        circle(pos_x + size/2*i, pos_y, size)

run()
