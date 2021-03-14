 ################################################################################
# Date: 02/09/2021
# Author: Jacob Kutcka
# This program takes the quantity of packages
# and calculates the price based on a discount
################################################################################

# Ask user for package discount
package = int(input("Please input the number of packages to be purchased: "))

# Check if 'package' is positive
if(package >= 0):
    # Check if 'package' is less than 10
    if(package <= 9):
        discount = 0
    # Check if 'package' is less than 20
    elif(package <= 19):
        discount = .1
    # Check if 'package is less than 50'
    elif(package <= 49):
        discount = .25
    # Check if 'package' is less than 100
    elif(package <= 99):
        discount = .35
    # Check if 'package' is greater than 99
    else:
        discount = .45

    price = package*99

    if(discount != 0):
        price = round(price - (price * discount),2)
        print('  ' + str(int(discount*100)) + '% discount applied.')
    else:
        print('  No discount applied.')
    print('  The final price for purchasing ' + str(package) + ' packages is $' + str(format(price, ',.2f')) + '.')
# If 'package' is negative
else:
    print('  Invalid Input!')
