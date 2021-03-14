################################################################################
# Date: 02/09/2021
# Author: Jacob Kutcka
# This program puts colors on a roulette
# wheel based on user's input as number (int)
################################################################################

# Ask user for Input
number = int(input('Please enter a pocket number: '))

# Check if number is within range
if(number >= 0 and number <= 36):
    #check if number is zero
    if(number == 0):
        print('  Pocket ' + str(number) + ' is green.')
    #check if (num is (even (between 1 and 10) or (between 19 and 28)) or (odd (between 11 and 18) or (between 29 and 36))
    elif((number%2 == 0 and ((number >=1 and number <= 10) or (number >= 19 and number <= 28))) or (number%2 == 1 and ((number >=11 and number <= 18) or (number >= 29 and number <= 36)))):
        print('  Pocket ' + str(number) + ' is black.')
    #check if (num is (odd (between 1 and 10) or (between 19 and 28)) or (even (between 11 and 18) or (between 29 and 36))
    else:
        print('  Pocket ' + str(number) + ' is red.')
else:
    print('  Invalid Input!')
