################################################################################
# Date: 03/01/2021
# Author: Jacob Kutcka
# This program takes a year count and monthly rainfall
# and calculates the total and monthly average rainfall during that period
################################################################################


def main():
    # Call input for starting number
    start = int(input("Starting number, in million: "))
    # Call input for average increase
    avg = int(input('Average daily increase, in percent: '))
    # Call input for day count
    days = int(input('Number of days to multiply: '))

    # Begin print table decor
    print('Day   Approx. Pop')
    # Begin loop for each day
    for i in range(days):
        # Reformat for printing
        pop = format(start, ',.4f')
        # Print each line
        print('{:>3}'.format(i+1) + '{:>14}'.format(pop))
        # Calculate tomorrow's population
        start += start * avg/100

if __name__ == '__main__':
    main()
