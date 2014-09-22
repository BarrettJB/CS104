#
# CS104, Lab 2: Compute Circumference and Area.
# Barrett Bryson bb36
# Emily Floch ecf3
# 9-11-2014
#
from __future__ import division, print_function
input = raw_input
inputdays= int(input("Enter a number of days:")) #get input from user
nweeks=inputdays//7 #calculate number of weeks
ndays=inputdays%7 #calculate number of days
print(inputdays,"days is",nweeks,"weeks and",ndays,"days.") #print results

