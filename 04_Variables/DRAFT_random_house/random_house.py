# The random() function (Random House Exercise)
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

# different from Processing: a boolean used to control `draw` from
# `mouse_pressed`
blackout = False

def setup():
    size(640, 460)
    frame_rate(5)  # sketch will refresh 5 times per second

def draw():
    global blackout

    # react to the mouse click using a boolean
    if blackout:
        background(0)
        blackout = False
        return

    # Sky
    background(50, 50, 250)
    rect_mode(CORNER)

    # Grass
    fill(25, 200, 25)
    rect(0, height / 2, width, height / 2)  # Draw grass

    x = width / 2
    y = height / 2
    w = random(150, 400)
    r = random(0.2, 1)  # scale ratio
    h = w * r
    sw = random(2, 4)  # thickness of line
    stroke_weight(sw)
    stroke(0)

    # House
    rect_mode(CENTER)
    fill(random(100, 255), 0, random(100, 255))
    rect(x, y, w, w * r)

    # Roof
    random_height = random(h / 2 + 50, 200)
    fill(random(50, 255), random(0, 50), random(0, 50))
    triangle(x - w / 2, y - (w * r) / 2, x + w / 2, y - (w * r) / 2, x, y - random_height)

    # Windows
    window_width = random(10, h / 3)
    window_pos_x = random(window_width, w / 2 - window_width)
    stroke_weight(2)
    stroke(0)
    fill(random(100, 255), random(100, 255), random(100, 255))
    rect(x - window_pos_x, y - (w * r) / 4, window_width, window_width)
    rect(x + window_pos_x, y - (w * r) / 4, window_width, window_width)
    line(x - window_pos_x, y - (w * r) / 4 - window_width / 2, x - window_pos_x, y - (w * r) / 4 + window_width / 2)
    line(x - window_pos_x - window_width / 2, y - (w * r) / 4, x - window_pos_x + window_width / 2, y - (w * r) / 4)
    line(x + window_pos_x, y - (w * r) / 4 - window_width / 2, x + window_pos_x, y - (w * r) / 4 + window_width / 2)
    line(x + window_pos_x - window_width / 2, y - (w * r) / 4, x + window_pos_x + window_width / 2, y - (w * r) / 4)

    # Door
    no_stroke()
    fill(random(100, 255), random(100, 255), random(100, 255))
    rect(x, y + h / 4, h / 4, h / 2 - sw * 2)
    fill(random(0, 50), random(0, 50), random(0, 50))
    circle(x - h / 24, y + h / 4, h / 12)

def mouse_pressed():
    global blackout
    print("Mouse pressed")
    # TODO: why this is not working still under investigation
    # background(0)
    blackout = True

run()
