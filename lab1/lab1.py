#
# Lab 1, CS104
# Barrett Bryson 1252391
# Caleb Bieske 2219011
# 9-4-2014
#
from __future__ import division, print_function
input = raw_input
from myro import *

init("COM40")
print("Done connecting")

# Make the robot draw a circle by making the left wheel
# go forward at speed 0.4, and the right wheel go forward
# at speed 0.75.  Stop the robot after 30 seconds.
print("Issuing motors command")
robot.motors(0.4, 1)
print("Doing nothing for 20 seconds")
wait(20)
print("Issuing stop command")
stop()
print("Done")