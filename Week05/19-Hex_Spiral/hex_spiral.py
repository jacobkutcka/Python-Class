################################################################################
# Author: Jacob Kutcka
# Date: Mar 12, 2021
# This program loops through 40 times to make
# a line 6 pixels longer and 60 degrees off from the last
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width('5')
    # --------------------------------------------------------------------------

    # Write your code here
    i=6
    while(i<240):
        forward(i)
        right(60)
        i+=6

# Don't change this
if __name__ == '__main__':
    main()
    done()
