###############################################################################
# Author: Jacob Kutcka
# Date: mar 18, 2021
# This program will print out vowels once at random
###############################################################################

from turtle import *
from math import *

def draw_a():
    penup()
    setheading(0)
    forward(60)
    setheading(90)
    forward(30)
    pendown()
    circle(30)
    forward(30)
    backward(60)
    penup()
    setheading(0)
    forward(10)

def draw_e():
    penup()
    setheading(90)
    forward(30)
    setheading(0)
    pendown()
    forward(60)
    left(90)
    circle(30,310)
    penup()
    setheading(90)
    forward(30*cos(310))
    setheading(0)
    forward(30*sin(310))

def draw_i():
    penup()
    setheading(0)
    forward(30)
    pendown()
    setheading(90)
    forward(60)
    penup()
    forward(30)
    dot(9)
    penup()
    backward(90)
    setheading(0)
    forward(40)

def draw_o():
    penup()
    setheading(0)
    forward(30)
    pendown()
    circle(30)
    penup()
    setheading(0)
    forward(50)

def draw_u():
    penup()
    setheading(90)
    forward(60)
    pendown()
    setheading(270)
    forward(30)
    circle(30,180)
    forward(30)
    backward(60)
    penup()
    setheading(0)
    forward(10)


def main():
    # You can use this for your own testing.

# Don't change this -----------------------------------------------------------
    if __name__ == '__main__':
        main()
        done()
