# Project 6 - Image Art
# CS 111, Reckinger
# 11/19/22
# Hiba Mirza
# User enters a filename in main.py
# The file image is drawn through turtle graphics with 6 different turtle shapes, all different sizes
# Images with bright red pixels are enhanced

import turtle
import random
from image import FileImage  # Adjusted import statement

# Create screen
s = turtle.getscreen()
s.colormode(255)
s.tracer(0)

# Create turtle
t = turtle.Turtle()
t.hideturtle()
t.penup()

# List for all possible turtle shapes
shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

# Change filename inside quotations (image1.gif, image2.gif, image3.gif)
filename = "image3.gif"

# Changes background color depending on the chosen image
if (filename == 'image1.gif' or filename == 'image2.gif'):
    s.bgcolor('white')
elif (filename == 'image3.gif'):
    s.bgcolor('black')

img = FileImage(filename)  # Use the correct class name
# Get height and width of image
width = img.get_width()
height = img.get_height()

# Loop through every 5 pixels in every row
for row in range(0, height, 5):
    # Loop through every 5 pixels in every column
    for col in range(0, width, 5):
        p = img.get_pixel(col, row)
        # If the amount of red in the pixel is higher than the green or blue (multiplied by 1.5), enhance the red even more
        if (p.red > 1.5 * p.green or p.red > 1.5 * p.blue):
            r = min(int(p.red * 1.8), 255)
            g = min(int(p.green * 1.6), 255)
            b = min(int(p.blue * 1.4), 255)
        else:
            # Keep the RGB the same
            r = min(int(p.red), 255)
            g = min(int(p.green), 255)
            b = min(int(p.blue), 255)

        t.pencolor(r, g, b)
        t.fillcolor(r, g, b)
        # Randomizes the size of the turtle from any size between 1-13
        # Default turtle size is 20
        t.turtlesize(random.randint(1, 13) / 20)
        # Randomizes the angle the turtle is facing
        # Any angle between 0-360
        t.right(random.randint(0, 360))
        t.begin_fill()
        # Randomly chooses one of the shapes in the list and makes it the shape of the turtle
        t.shape(random.choice(shapes))
        t.stamp()
        # Places turtle 200 to the left
        x = col - 200
        # Places turtle 200 down
        # Multiply '-1' in order to keep the image from drawing upside down
        y = -1 * (row - 200)
        t.goto(x, y)
    t.penup()
    t.end_fill()
    s.update()

turtle.mainloop()
