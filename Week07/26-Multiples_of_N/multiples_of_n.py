################################################################################
# Author: Jacob Kutcka
# Date: Mar 23, 2021
# This program will list off the numbers of the original list, then
# ask the user for a number. It will then list the numbers that are multiples
# of the user's input
################################################################################

def main():

    number_list = [19, 2940, -189, 10, 28, -58, 1, 85, 201, -15, 122, 799, 406]
    factor = 7
    print('Original list of numbers:')
    print(number_list)
    print('Numbers in the list that are multiples of ' + str(factor) + ':')
    # Call up multiples_of() function
    print(multiples_of(factor, number_list))

def multiples_of(factor, number_list):
    list = []
    # Loop each number
    for i in range(len(number_list)):
        if number_list[i] % factor == 0:
            list.append(number_list[i])
    return list
if __name__ == '__main__':
    main()
