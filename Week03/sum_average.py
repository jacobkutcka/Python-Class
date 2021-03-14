################################################################################
# Date: 02/17/2021
# Author: Jacob Kutcka
# This program takes a set of positive numbers from the user
# and calculates the sum and average of said numbers
################################################################################

def main():
    sum, count, average = 0, 0, 0
    # Ask user for num
    num = float(input('Enter a non-negative number (negative to quit): '))
    # Until neg num input, continue loop
    while num >= 0:
        # Add input to sum
        sum += num
        # +1 to count
        count += 1
        # Ask user for input
        num = float(input('Enter a non-negative number (negative to quit): '))

    if sum == 0:
        # If first input was negative, return "no input"
        print('No input.')
    else:
        # calculate average and print sum and average
        average = sum / count
        print('Sum = ' + str(format(sum, ',.2f')))
        print('Average = ' + str(format(average, ',.2f')))

if __name__ == '__main__':
    main()
