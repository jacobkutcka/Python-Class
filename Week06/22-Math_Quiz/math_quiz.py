###############################################################################
# Author: Jacob Kutcka
# Date: Mar 18, 2021
# This program will generate 2 random numbers, calculate the sum
# and ask the user for their guess. Tell if they're correct or not
###############################################################################

import random

def main():
    # Write your mainline logic here ------------------------------------------
    top = random_number(2)
    bottom = random_number(3)
    sum = int(top) + int(bottom)
    print('{:>5}'.format(top) +'\n+{:>4}'.format(bottom) + '\n-----')
    answer = input('= ')
    if int(answer) == int(sum):
        print('Correct -- Good Work!')
    else:
        print('Incorrect. The correct answer is ' + str(sum) + '.')
def random_number(count):
    if count == 2:
        output = random.randint(10,99)
    else:
        output = random.randint(100,999)
    return output
# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
