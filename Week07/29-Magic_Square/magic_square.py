################################################################################
# Author:
# Date:
# Description ...
################################################################################

def main():

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    m3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]

    # Section for M1
    print_square(m1)


    # Section for M2

    # Section for M3
def print_square(set):
    print('Your square is:')
    for r in range(3):
        for c in range(3):
            print(f'{set[r][c]:2d}', end=' ')
        print()

if __name__ == '__main__':
    main()
