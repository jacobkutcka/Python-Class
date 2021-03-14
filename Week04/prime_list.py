################################################################################
# Date: 03/08/2021
# Author: Jacob Kutcka
# This program takes every number below the user's limit
# and checks if each number is prime. If so, list them at the end
################################################################################

def main():
    # Ask user for input
    max = int(input("Enter a positive integer: "))
    # Initialize list
    list = []
    for i in range(max+1):
        # If within range and prime number, add to list
        if is_prime(i) == True:
            list.append(str(i))
    # Initialize output and begin adding
    output = "The primes up to " + str(max) + " are :"
    # For each number but the last, add with a comma
    for i in range(len(list)-1):
        output += " " + list[i] + ","
    # For last number, don't add comma
    output += " " + list[len(list)-1]
    # Print output
    print(output)


def is_prime(num):
    # Failsafe for '1'
    if num == 1:
        return(False)
    else:
        # If the number is evenly divisable by a number below half it's value and 2, return true
        for i in range(2, int(num/2)+1):
            if num % i == 0:
                return(False)
        # Fail all other options, return false
        return(True)

if __name__ == '__main__':
    main()
