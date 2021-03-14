################################################################################
# Author: Jacob Kutcka
# Date: Mar 12, 2021
# This program will automatically solve the maze
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    bgpic('maze.png')
    shape('turtle')
    color('green')
    width('5')
    step = 12
    # --------------------------------------------------------------------------

    # Write your code here
    #right
    forward(13)
    left(90)
    #up
    forward(37)
    right(90)
    #right
    forward(22)
    left(90)
    #up
    forward(70)
    left(90)
    #left
    forward(22)
    right(90)
    #up
    forward(98)
    right(90)
    #right
    forward(23)
    left(90)
    #up
    forward(23)
    right(90)
    #right
    forward(190)
    right(90)
    #down
    forward(227)
    left(90)
    #right
    forward(30)

# Don't change this
if __name__ == '__main__':
    main()
    done()
