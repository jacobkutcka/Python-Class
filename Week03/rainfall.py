################################################################################
# Date: 03/01/2021
# Author: Jacob Kutcka
# This program takes a year count and monthly rainfall
# and calculates the total and monthly average rainfall during that period
################################################################################

def main():
    # Establish sum
    sum = 0
    # Call for year count
    years = int(input('Enter the number of years: '))
    if years > 0:
        # Loop for each year
        for i in range(years):
            print('  For year No. ' + str(i+1))
            # Add sum of rainfall in subject year
            sum += year(i)
        print('There are ' + str(years*12) + ' months.')
        print('The total rainfall is ' + str(format(sum, ',.2f')) + ' inches.')
        print('The monthly average rainfall is ' + str(format(sum/(years * 12), ',.2f')) + ' inches.')
    else:
        print("Invalid input.")

def year(year):
    # Establish month list and sum
    sum = 0
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # Loop for each month
    for i in range(len(months)):
        # Find rain for subject month
        rainfall = float(input('    Enter the rainfall for ' + months[i] + '.: '))
        while(rainfall < 0):
            # If rainfall is negative, inform user and ask again
            print('    Invalid input, please try again.')
            rainfall = float(input('    Enter the rainfall for ' + months[i] + '.: '))
        # Add together all months' rainfall
        sum += rainfall
    # return rainfall sum
    return sum


if __name__ == '__main__':
    main()
