###############################################################################
# Author: Jacob Kutcka
# Date: mar 18, 2021
# This program will print out vowels once at random
###############################################################################

from turtle import *

# Add your imports here -------------------------------------------------------
import random
from vowels import *

def main():
    # Don't change this block -------------------------------------------------
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)
    # -------------------------------------------------------------------------


    # Write your mainline logic here ------------------------------------------
    vowels = ['a', 'e', 'i', 'o', 'u']
    l = random.choices(vowels)
    for i in range(4):
        if l[i] == 'a':
           draw_a()
        elif l[i] == 'e':
           draw_e()
        elif l[i] == 'i':
           draw_i()
        elif l[i] == 'o':
           draw_o()
        else: #l[i] == 'u'
           draw_u()


# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
    done()
