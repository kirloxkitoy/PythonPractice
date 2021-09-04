#!/usr/bin/python
import sys
from datetime import datetime


_pi=3.1416
_radius=1.1
#Excercise 1 Word formats
print("Twinkle, twinkle, little star," "\n\t\tHow I wonder what you are!""\n\t\t\t\t\tUp above the world so high,""\n\t\t\t\t\tLike a diamond in the sky.","\nTwinkle, twinkle, little star,""\n\t\tHow I wonder what you are")

#Excercise 2 Python version
print("python version")
print(sys.version)

#Excercise 3 
print(datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))

#Excercise 4
radius = input("Input radius:")
rads = (float(radius)*float(radius))
area = _pi * rads
print(str(area))

#Excercise 5
name = input()
rev_str = name[::-1]
print(rev_str)