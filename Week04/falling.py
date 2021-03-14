################################################################################
# Date: 02/26/2021
# Author: Jacob Kutcka
# This program takes the equation d=1/2gt^2
# and calculates the fall distance of said object
################################################################################

# Write function(s) here

def main():
    # Write your 'mainline logic' here

    print("Time (s)  Distance (m)")
    print("----------------------")
    for i in range(1,11):

        distance = format(falling_distance(i), ',.2f')
        print('{:>8}'.format(i) + '{:>14}'.format(distance))

def falling_distance(time):
    # Calculate distance falling
    distance = .5 * 9.81 * time ** 2
    return distance

if __name__ == '__main__':
    main()
