lineWeight = 10		        # Sets thickness of all turtles
turtleColor = "black"		# Sets color of all turtles
screenColor = "purple"		# Sets screen color
iconSize = 490                  # Sets size of Icon

import turtle			# turtle stuff
wn = turtle.Screen()
wn.bgcolor(screenColor)

cloak = turtle.Turtle()		# This turtle makes the triangle
cloak.color(turtleColor)
cloak.pensize(lineWeight)
cloak.shape("blank")

wand = turtle.Turtle()		# This turtle makes the line
wand.color(turtleColor)
wand.pensize(lineWeight)
wand.shape("blank")

stone = turtle.Turtle()		# This turtle makes the circle
stone.color(turtleColor)
stone.pensize(lineWeight)
stone.shape("blank")

for name in [cloak,wand,stone]:
    name.up()
    name.right(90)
    name.forward(int(iconSize*((3**.5)/6)))
    name.left(90)
    name.down()

wand.left(90)
wand.forward(int(iconSize*((3**.5)/2)))

stone.circle(int(iconSize*((3**.5)/6)))

cloak.up()
cloak.right(180)
cloak.forward(iconSize/2)
cloak.right(180)
cloak.down()
for sides in range(0,3):
    cloak.forward(iconSize)
    cloak.left(120)

wn.exitonclick()
