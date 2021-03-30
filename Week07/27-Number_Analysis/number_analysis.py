################################################################################
# Author: Jacob Kutcka
# Date: Mar 29, 2021
# This program will take in 10 numbers from the user and
# calculate the min, max,sum, and average
################################################################################

def main():
    numbers = get_number_list()

    # Lowest number
    print('Lowest number: ' + str(format(min(numbers), '.2f')))
    # Greatest number
    print('Highest number: ' + format(max(numbers), '.2f'))
    # Sum of numbers
    print('Total: ' + str(format(sum(numbers), '.2f')))
    # Average of numbers
    print('Average: ' + str(format(sum(numbers)/10.0, '.2f')))

def get_number_list():
    list = []
    for i in range(1,11):
        list.append(input('  Enter number {:>2}'.format(i) + ' of 10: '))
    return list

if __name__ == '__main__':
    main()
