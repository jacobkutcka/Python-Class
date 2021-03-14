################################################################################
# Author: Jacob Kutcka
# Date: 02/09/2021
# This program displays the number of days
# in Feburary on any given year
################################################################################

# Ask user for year in integer form
year = int(input("Please input a year: "))

# Find if the year is divisible by 100
if year%100 == 0:
    # If divisible by 100, check if divisible by 400
    if year%400 == 0:
        # If true, leap year
        days = 29
    # If not divisible by 400, not leap year
    else:
        days = 28
# If not divisible by 100, check 4
elif year%4 == 0:
        # If true, leap year
        days = 29
# If all return false, not leap year
else:
    days = 28

# Print final script to user
print('In the year ' + str(year) + ', there are ' + str(days) + ' days in February.')
