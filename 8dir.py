import turtle as t
import random
from math import sqrt

# Set up the canvas
SIZE = 10_000
USE_COLOURS = True
DISTANCE = 10

t.setup(SIZE, SIZE)

# Create a turtle object
pen = t.Turtle()

# Create a dictionary mapping numbers to colors
color_dict = {0: 'red', 1: 'blue', 2: 'green', 3: 'yellow',
              4: 'purple', 5: 'orange', 6: 'pink', 7: 'brown'}

# Loop 100,000 times
for _ in range(100_000):
    dir = random.randint(0, 7)
    # Set the direction to 45 * dir degrees
    pen.setheading(45 * dir)
    # Set the color based on the direction
    if USE_COLOURS:
        pen.color(color_dict[dir])
    else:
        pen.color("black")
    # Move the turtle forward by 1 unit
    if dir % 2 == 0:
        dist = sqrt(2) * DISTANCE
    else:
        dist = DISTANCE

    pen.forward(dist)

# Keep the window open until it is closed manually
t.done()