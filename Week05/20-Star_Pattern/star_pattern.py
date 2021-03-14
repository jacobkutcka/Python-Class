################################################################################
# Author: Jacob Kutcka
# Date: Mar 12, 2021
# This program will take the number of sides from the user
# and draw a star with the proper angles for the sides given
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()
    # --------------------------------------------------------------------------

    # Write your code here
    points = int(input("How many sides: "))

    a = 360/points
    b = 2*a

    left(b/2)

    for i in range(points):
        right(a)
        forward(side_length)
        left(b)
        forward(side_length)


# Don't change this
if __name__ == '__main__':
    main()
    done()
