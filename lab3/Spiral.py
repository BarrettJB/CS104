
from __future__ import division, print_function
input = raw_input
from myro import *

# connect to the robot
init("COM40")

speed = 1           #speed of scribbler      
innerRatio = .5     #makes left wheel go slower by given ratio 
outerRatio = .7     #makes left wheel go slower by given ratio. Needs to be larger than innerRatio
numTimes = 20       #Number of points on spiral
armLength = 1       #length of points on spiral 

# draw a spiral
for i in range(numTimes):
     #makes outer curve
    robot.motors(speed*outerRatio,speed)
    wait(armLength)
    #makes inner curve
    robot.motors(-speed*innerRatio,-speed) 
    wait(armLength)
    #moves the direction
    robot.motors(0,speed)
    wait(.5)
    
robot.motors(0,0)