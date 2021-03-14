################################################################################
# Date: 02/26/2021
# Author: Jacob Kutcka
# This program takes a set of integers
# and calculates which one of the two is greater
################################################################################


def main():
    # Ask user for first number
    first_number = int(input("Enter the first integer: "))
    # Ask user for second number
    second_number = int(input("Enter the second integer: "))

    if max_of_two(first_number, second_number) == True:
        print(str(first_number) + " is greater")
    else:
        print(str(second_number) + " is greater")

def max_of_two(first_number, second_number):
    # Calculate which number is greater
    if(first_number<second_number):
        return(True)
    else:
        return(False)

if __name__ == '__main__':
    main()
