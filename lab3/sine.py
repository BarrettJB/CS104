#
# CS104 Lab 3: Making a turtle graph a sine wave
# Barrett Bryson
# Emily Floch
# <September 18, 2014
#

import turtle
import math
wn = turtle.Screen()

wn.setworldcoordinates(0, -1, 360, 1)      #sets screen so that whole curve can be seen

todd = turtle.Turtle()

for angle in range(360):
    x = angle                           #setting x coordinate for todd
    y = math.sin(math.radians(angle))   #setting y coordinate for todd
    todd.goto(x, y)                      #goes to defined position
    
wn.exitonclick()