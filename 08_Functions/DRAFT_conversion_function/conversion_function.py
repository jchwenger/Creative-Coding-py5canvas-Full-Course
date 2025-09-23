# Conversion Function
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

measurement = 0
fahrenheit = 0
celsius = 0
min_num = 32  # min measurement
max_num = 330  # max measurement

def setup():
    global measurement
    size(640, 360)
    measurement = select_num()

def mouse_pressed():
    global measurement
    measurement = select_num()

def draw():
    global fahrenheit, celsius
    background(255)
    # Position of lines
    x1 = width/6
    x2 = width - width/6
    f_line = height/4  # top line (fahrenheit)
    c_line = height - height/4  # bottom line (celsius)

    stroke_weight(80)
    # blendMode() blends the pixels in the display window according to a defined mode.
    # blendMode(BLEND) is the default.

    # Gray background lines
    # TODO: blendMode(BLEND) - not implemented in py5canvas yet
    stroke(230)
    line(x1, f_line, x2, f_line)
    line(x1, c_line, x2, c_line)

    # Black lines (update with every new measurement)
    stroke(0)

    # lerp() calculates a number between two numbers at a specific increment.
    # It is convenient for creating motion along a straight path.
    # Try un-commenting the alternative to see how the line length changes from
    # a gradual motion to instantaneous update.
    fahrenheit = lerp(fahrenheit, measurement, 0.05)
    celsius = lerp(celsius, fahrenheit_to_celsius(measurement), 0.05)

    # ----ALTERNATIVE-----
    # fahrenheit = measurement
    # celsius = fahrenheit_to_celsius(measurement)

    line(x1, f_line, x1 + fahrenheit, f_line)
    line(x1, c_line, x1 + celsius, c_line)

    text_size(14)
    fill(255)
    # blendMode(DIFFERENCE) subtracts colors from the underlying image/shape so
    # when the black line is over the text, the text is white. Otherwise,
    # the text is black (legibility).
    # TODO: blendMode(DIFFERENCE) - not implemented in py5canvas yet
    text_align(CENTER, CENTER)

    # Use the round() function to round to the nearest degree.
    text(str(round(fahrenheit_to_celsius(measurement))) + "° CELSIUS", width/2, c_line)
    text(str(round(measurement)) + "° FAHRENHEIT", width/2, f_line)

def select_num():
    return random(min_num, max_num)

def fahrenheit_to_celsius(deg_f):
    return (deg_f - 31) * 5/9

run()
