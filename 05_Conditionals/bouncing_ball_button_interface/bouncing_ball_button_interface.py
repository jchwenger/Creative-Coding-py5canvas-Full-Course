# Button interface / bouncing ball
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

# Declare ball variables
x = 0
y = 0
radius = 0
xspeed = 0
yspeed = 0
col = None
going = True

# Declare button variables
button_size = 160
padding = 40  # spacing between buttons
color_button_x = 0
stop_button_x = 0
radius_button_x = 0  # x pos of buttons
over_color_button = False
over_stop_button = False
over_radius_button = False

def setup():
    global x, y, radius, xspeed, yspeed, col, color_button_x, stop_button_x, radius_button_x
    size(640, 360)
    rect_mode(CENTER)

    # Text properties
    text_align(CENTER, CENTER)
    text_size(20)

    # Make the circle a random color
    col = color(random(255), random(255), random(255))

    radius = 25
    xspeed = 3
    yspeed = 3

    # position of ball
    x = random(radius, width-radius)
    y = random(radius, height-radius)

    # x position of the buttons
    color_button_x = width/2 - button_size - padding
    stop_button_x = width/2
    radius_button_x = width/2 + button_size + padding

def draw():
    global x, y, xspeed, yspeed, over_color_button, over_stop_button, over_radius_button
    background(0)
    no_stroke()

    if going:
        x = x + xspeed
        y = y + yspeed

    if x < radius or x > width - radius:
        xspeed = xspeed * -1

    if y < radius or y > height - radius:
        yspeed = yspeed * -1

    # ------------colorButton----------------
    if (mouse_x > color_button_x - button_size/2 and mouse_x < color_button_x + button_size/2
        and mouse_y > height/2 - button_size/2 and mouse_y < height/2 + button_size/2):
        over_color_button = True  # the mouse is over the button
        fill(255)
        square(color_button_x, height/2, button_size)
    else:
        over_color_button = False

    # -----------start/stop button------------
    if (mouse_x > stop_button_x - button_size/2 and mouse_x < stop_button_x + button_size/2
        and mouse_y > height/2 - button_size/2 and mouse_y < height/2 + button_size/2):
        over_stop_button = True  # the mouse is over the button
        fill(255)
        square(stop_button_x, height/2, button_size)
    else:
        over_stop_button = False

    # ------------radius button----------------
    if (mouse_x > radius_button_x - button_size/2 and mouse_x < radius_button_x + button_size/2
        and mouse_y > height/2 - button_size/2 and mouse_y < height/2 + button_size/2):
        over_radius_button = True  # the mouse is over the button
        fill(255)
        square(radius_button_x, height/2, button_size)
    else:
        over_radius_button = False

    # draw buttons
    stroke(255)
    no_fill()
    square(color_button_x, height/2, button_size)
    square(stop_button_x, height/2, button_size)
    square(radius_button_x, height/2, button_size)

    # draw button labels
    fill(255)
    text("Color", color_button_x, height/2 + button_size/2 + padding/2)
    text("Start/Stop", stop_button_x, height/2 + button_size/2 + padding/2)
    text("Size", radius_button_x, height/2 + button_size/2 + padding/2)

    # draw ball
    fill(col)
    no_stroke()
    circle(x, y, radius*2)

def mouse_pressed():
    global col, going, radius
    if over_color_button:
        # change ball to random color
        col = color(random(255), random(255), random(255))

    if over_stop_button:
        # stop or start the ball
        going = not going

    if over_radius_button:
        # change the radius
        radius = random(10, 100)

run()
