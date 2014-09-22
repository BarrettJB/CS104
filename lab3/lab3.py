#
# CS104 Lab 3: Making a turtle graph a sine wave
# Barrett Bryson
# Emily Floch
# <September 18, 2014
#

from __future__ import division, print_function
input = raw_input
from myro import *

# connect to the robot
init("COM40")

speed = 1           #speed of scribbler
numSeconds = 2      #number of seconds moving forward
leftSeconds = .3    #number of seconds turning left 
numTimes = 25       #number of sides on spiral

# draw a spiral
for i in range(numTimes):
    forward(speed,numSeconds)
    turnLeft(speed,leftSeconds)
    
