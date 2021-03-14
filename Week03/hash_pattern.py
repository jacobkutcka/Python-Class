################################################################################
# Date: 02/17/2021
# Author: Jacob Kutcka
# This program takes a number from the user
# and produces a slant of '#' characters
################################################################################

# Ask user for Input
INPUT = int(input('Enter the number of lines: '))
# Begin loop between 0 and INPUT
for i in range(INPUT):
    # Begin output
    output = '#'
    # Count spaces requried
    for c in range(i):
        # Add spaces to output
        output += ' '
    # Add final '#' to output
    output += '#'
    # Print output
    print(output)
