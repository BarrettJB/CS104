#
# CS104, Lab 2: Compute Circumference and Area.
# Barrett Bryson bb36
# Emily Floch ecf3
# 9-11-2014
#
from __future__ import division, print_function
input = raw_input
import math
#get inputs from user
L = float(input("Enter length of pendulum(cm):")) 
alpha = float(input("Enter angle of displacement(radians):"))
#constants used later
g = 980 #cm/s^2
pi = 3.14159
#period of pendulum equation
p = (2*pi)*((L/g)**.5)*(1+(.25*(math.sin(alpha/2))**2))
#output calculated values
print("The period of the pendulum is",p,"seconds. Given that length:",L,"cm and angle of displacement:", alpha, "radians")