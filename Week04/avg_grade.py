################################################################################
# Date: 02/26/2021
# Author: Jacob Kutcka
# This program takes grade percentage
# and calculates the letter per grade and average
################################################################################

def main():
    sum = 0
    for i in range(5):
        num = get_valid_score()
        sum += num
        determine_grade(num)
    calc_average(sum)

def get_valid_score():
    valid = False
    # Loop until valid number entered
    while(valid == False):
        # Call for score
        score = int(input("Enter a score: "))
        # Check score for validity
        if(score<0 or score>100):
            print("Invalid Input. Please try again.")
        else:
            # End loop
            valid = True
            # Return score
            return score

def determine_grade(number):
    if(number>=90):
        letter = "A"
    elif(number>=80):
        letter = "B"
    elif(number>=70):
        letter = "C"
    elif(number>=60):
        letter = "D"
    else:
        letter = "F"
    print("The letter grade for " + str(format(number, '.1f')) + " is " + letter + ".")

def calc_average(sum):
    avg = sum/5.0
    print("The average score is " + str(format(avg, '.2f')) + ".")

if __name__ == '__main__':
    main()
