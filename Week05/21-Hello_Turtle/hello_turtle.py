################################################################################
# Author: Jacob Kutcka
# Date: Mar 12, 2021
# This program will print out
# 'hello turtle' using turtle
################################################################################

# Don't change this
from turtle import *

def draw_e():
    # Write this function
    penup()
    setheading(90)
    forward(30)
    setheading(0)
    pendown()
    forward(60)
    left(90)
    circle(30,310)


def draw_h():
    # Write this function
    pendown()
    setheading(90)
    forward(120)
    backward(90)
    circle(-30,180)
    setheading(270)
    forward(30)

def draw_l():
    # Write this function
    penup()
    setheading(0)
    forward(10)
    pendown()
    setheading(90)
    forward(120)
    backward(120)
    penup()
    setheading(0)
    forward(10)

def draw_o():
    # Write this function
    penup()
    setheading(0)
    forward(30)
    pendown()
    circle(30)
    penup()
    setheading(0)
    forward(30)
def draw_r():
    # Write this function
    setheading(90)
    pendown()
    forward(60)
    back(30)
    circle(-30,90)
    penup()
    setheading(270)
    forward(60)

def draw_t():
    # Write this function
    penup()
    setheading(90)
    forward(90)
    setheading(0)
    pendown()
    forward(60)
    backward(30)
    setheading(90)
    forward(30)
    backward(120)
    penup()
    setheading(0)
    forward(30)

def draw_u():
    # Write this function
    penup()
    setheading(90)
    forward(60)
    pendown()
    setheading(270)
    forward(30)
    circle(30,180)
    forward(30)
    backward(60)
    setheading(0)
    penup()

def draw_space():
    penup()
    setheading(0)
    forward(30)

def main():

    # Don't change this block --------------------------------------------------
    setup(600, 400)
    width(9)
    # --------------------------------------------------------------------------

    # Write your main function code here
    penup()
    #begin lining up text
    goto(-250, 30)
    draw_h()
    draw_space()
    draw_e()
    draw_space()
    draw_l()
    draw_space()
    draw_l()
    draw_space()
    draw_o()

    #line up second line
    goto(-280, -125)
    draw_t()
    draw_space()
    draw_u()
    draw_space()
    draw_r()
    draw_space()
    draw_t()
    draw_space()
    draw_l()
    draw_space()
    draw_e()


# Don't change this
if __name__ == '__main__':
    main()
    done()
