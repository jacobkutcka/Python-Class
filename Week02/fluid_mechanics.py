################################################################################
# Date: 02/09/2021
# Author: Jacob Kutcka
# This program takes the velocity of water in a specific diameter pipe at a temp
# and calculates the Reynolds number for said situation
################################################################################

# Ask user for Input
# Velocity
velocity = float(input('Enter the velocity of water in the pipe: '))
# Diameter
diameter = float(input("Enter the pipe's diameter: "))
# Temperature
temp = float(input('Enter the temperature in °C as 5, 10, or 15: '))
# Convert temp to viscosity
if(temp == 5):
    visco = 1.49e-6
elif(temp == 10):
    visco = 1.31e-6
else:
    visco = 1.15e-6
# Do Math
number = (velocity * diameter) / visco
# Scientific notation editing to 2 decimal points
number = "{:.2e}".format(number)
# Print proper output
print('The Reynolds number for flow at ' + str(velocity) + ' m/s in a ' + str(diameter) + ' m diameter pipe at ' + str(float(temp)) + '°C is ' + str(number) + '.')
