#
# CS104, Lab 2: Compute Circumference and Area.
# Barrett Bryson bb36
# Emily Floch ecf3
# 9-11-2014
#
from __future__ import division, print_function
input = raw_input
pi = 3.14159 #used for later calculations
d_in = float(input("Diameter of circle(in):")) #get users input
r_cm = (d_in*2.54)*.5 #convert diameter in inches to radius in cm
circumference = 2*r_cm*pi #calculate circumference
area = (r_cm**2)*pi #calculate area
print("The circumference of your circle is",circumference,"cm") #output calculated values
print("The area of your circle is",area,"cm^2")