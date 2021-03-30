################################################################################
# Author: Jacob Kutcka
# Date: Mar 29, 2021
# This program will estimate the probability of rolling
# certian numbers on 2d6 rolls
################################################################################
import random

def main():
    roll_count = 900000

    totals = get_2d6_rolls(roll_count)

    print('Roll  Frequency')
    for i in range(11):
        percent = round(totals[i]*100/roll_count, 2)
        print('{:>3}'.format(i+2) + '{:>9}'.format(percent) + '%')

def get_2d6_rolls(roll_count):
    count = [0,0,0,0,0,0,0,0,0,0,0]
    for i in range(roll_count):
        sum = roll_d6() + roll_d6()
        count[sum-2] += 1
    return count

def roll_d6():
    return random.choice(range(1,6))

if __name__ == '__main__':
    main()
