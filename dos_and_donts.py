#-*- coding: utf-8 -*-

# Whitespace
# 4 spaces per indentation, no tabs
# One line between functions/methods
# Two lines between classes

# Don't
def foo(val):
        if val == 8:
                print("Value is 8")
def bar(a, b):
    really_long_summation_function_this_feels_like_java_wtf(a, b, func=int.__add__, result=True)
    return a + b

# Do
def foo(a, b):
    really_long_summation_function_this_feels_like_java_wtf(a,
                                                            b,
                                                            func=int.__add__,
                                                            result=True)
    return a + b

def bar(val):
    if val == 10:               # four spaces
        print("Value is 10")


# Imports
# Avoid wild card imports
# Module imports should be on separate lines
# Import should be grouped in order of specificity

# Don't
from os import *
import sys, random, csv
from mymodule import this
import urllib

# Do
import sys
import random
import csv
import urllib
from os import path, popen, getenv

from mymodule import this


# Naming conventions
# Variables, methods, functions should be:
# lowercase or lowercase_with_underscores
#
# Except for globals (top-level module variables)
# and constants, should be: UPPERCASE or UPPERCASE_WITH_UNDERSCORES
#
# Classes: FooBar, ACatGifToRemember, etc.
#
# Special conventions:
# _class_attribute -- weak "internal use" attribute
# __class_attribute -- does name mangling, i.e. Foo._Foo__class_attribute
# __foo__ -- "magic" methods, e.g. __init__, __add__, and more.

# Don't
pi = 3.14
def Area(Radius):
    return Radius * Radius * pi

class RECTANGLE:
    def __init__(self, Width, Height):
        self.Width = Width
        self.Height = Height

    def CalculateArea(self):
        return self.Width * self.Height


# Do
PI = 3.14

def area(radius):
    return radius * radius * pi


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Programming Recommendations

# Context Managers: use them if they're provided or write your own

# Don't
def read_file(filename):
    myfile = open(filename, 'r')
    contents = myfile.read()
    myfile.close()

# Do
def read_file(filename):
    with open(filename, 'r') as myfile:
        contents = myfile.read()


# Exceptions: don't use catch-all exceptions

# Don't
dictionary = {}
try:
    value = dictionary[key]
except:
    value = 10

# Do
try:
    value = dictionary[key]
except KeyError:
    value = 10

# Better
value = dictionary.get(key, 10)     # will return 10 if `key' doesn't exist

