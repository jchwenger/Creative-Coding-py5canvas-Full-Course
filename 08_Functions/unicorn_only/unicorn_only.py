# Rainbow, Unicorn, Puppy Functions
# The Coding Train / Daniel Shiffman
# Processing Intro Series
# Translated to py5canvas

from py5canvas import *

# Hex color support - yay, implemented in py5canvas!
rainbow_colors = ["#9A56FF", "#527AF2", "#F2B807", "#F28907", "#F2220F"]

def setup():
    size(640, 360)
    color_mode("hsb", 255)
    rect_mode(CENTER)
    background(150, 30, 255)
    rainbow()
    unicorn()

def draw():
    pass

def rainbow():
    sw = 15
    stroke_weight(sw)
    no_fill()

    for i in range(len(rainbow_colors)):
        stroke(rainbow_colors[i])  # pick a color from the array
        arc(width/2, (height + 100) - sw*i, width + sw*i, width, PI, PI*2)

def unicorn():
    sw = 3  # strokeWeight
    pos_x = width/2 - 110
    pos_y = height/2 + 50
    stroke(0)
    stroke_weight(sw)
    tri_size = 50  # size of triangle
    # pick a random horn color
    fill(rainbow_colors[int(random(len(rainbow_colors)))])
    triangle(pos_x - tri_size/2, pos_y - 100, pos_x + tri_size, pos_y - 90, pos_x + tri_size/2, pos_y - 100 - tri_size*2)

    # unicorn "mane"
    for i in range(7):
        fill(130, 100, 255)
        circle((pos_x - 40) - 10*i, pos_y - 50 + 40*i, 100)

    # head
    fill(255)
    rect(pos_x, pos_y, 150, 215, 100)

    # nose
    fill(0, 120, 255)
    ellipse(pos_x, pos_y + 60, 150, 110)

    # nostrils
    fill(0, 50, 255)
    ellipse(pos_x + 10, pos_y + 60, 10, 10)
    ellipse(pos_x - 10, pos_y + 60, 10, 10)

    # eyes
    fill(0)
    ellipse(pos_x, pos_y - 50, 5, 5)
    ellipse(pos_x + 10, pos_y - 50, 8, 8)

def puppy():
    sw = 3
    pos_x = width/2 + 110
    pos_y = height/2 + 50
    stroke(0)
    stroke_weight(sw)

    # ears
    for i in range(0, 30, 3):  # equivalent to for (float i = 0; i < 3; i+=0.3)
        fill(15, 150, 100)
        no_stroke()
        circle((pos_x - 50) - 10*i/10, pos_y - 55 + 40*i/10, 100)
        circle((pos_x + 50) + 10*i/10, pos_y - 55 + 40*i/10, 100)

    # head
    stroke(0)
    fill(15, 75, 200)
    rect(pos_x, pos_y, 150, 215, 100)

    # nose
    fill(35, 75, 255)
    ellipse(pos_x, pos_y + 60, 150, 110)

    # mouth
    fill(0)
    ellipse(pos_x, pos_y + 25, 70, 35)
    line(pos_x, pos_y + 25, pos_x, pos_y + 75)
    no_fill()
    arc(pos_x - 20, pos_y + 75, 40, 25, 0, PI)
    arc(pos_x + 20, pos_y + 75, 40, 25, 0, PI)

    # eyes
    fill(0)
    ellipse(pos_x - 25, pos_y - 25, 20, 20)
    ellipse(pos_x + 25, pos_y - 25, 20, 20)

    # eyebrows
    no_fill()
    arc(pos_x - 25, pos_y - 50, 40, 25, PI, 2*PI - PI/4)
    arc(pos_x + 25, pos_y - 50, 40, 25, PI + PI/4, 2*PI)

run()
