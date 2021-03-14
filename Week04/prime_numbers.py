################################################################################
# Date: 03/04/2021
# Author: Jacob Kutcka
# This program takes a number
# and checks if it is a prime number
################################################################################

def main():
    # Call for user input
    num = int(input("Enter a positive integer (-1 to quit): "))
    # If the number is positive
    while num > -1:
        # Check if prime
        prime = is_prime(num)
        if prime == False:
            # Print if false
            print(str(num) + ' is not a prime number.')
        else:
            # Print if true
            print(str(num) + ' is a prime number.')
        # Repeat loop
        num = int(input("Enter a positive integer (-1 to quit): "))

# Calculate if prime number
def is_prime(num):
    if num == 1:
        return(False)
    else:
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                return(False)
        return(True)

if __name__ == '__main__':
    main()
