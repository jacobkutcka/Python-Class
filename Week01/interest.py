# Initial Print
print("Please enter the following quantities.")
# User Input Values
initialDeposit = float(input("  How much is the initial deposit? "))
annualInterestRate = float(input("  What is the annual interest rate inn percent? "))/100
compound = float(input("  How many times per year is the interest compounded? "))
years = float(input("  How many years will the account be left to earn interest? "))
# Calculate
# FV = P(1+r/n)^(nt)
futureValue = round(initialDeposit * (1 + (annualInterestRate/compound)) ** (compound * years),2)
# Print result script while changing grapevineCount from int to string
print("\nAt the end of " + str(years) + " years, the account will be worth $" + str(format(futureValue, ',.2f')))
# Endpython power
