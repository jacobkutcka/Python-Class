################################################################################
# Date: 02/09/2021
# Author: Jacob Kutcka
# This program takes a time in seconds
# and calculates what it is in larger units
################################################################################

# Ask user for Input
initial = int(input('Please enter a time in seconds. '))
# Duplicate initial seconds count
seconds = initial
# Begin line to print
line = ''
# Check if less than one minute
if(seconds<60):
    line = '  The number of seconds is less than one minute.'
else:
    # Calculate days (if any)
    days = (seconds-seconds%86400)/86400
    # Subtract days worth of seconds from seconds
    seconds -= days*86400
    # Calculate hours (if any)
    hours = (seconds-seconds%3600)/3600
    # Subtract hours worth of seconds from seconds
    seconds -= hours*3600
    # Calculate days (if any)
    minutes = (seconds-seconds%60)/60
    # Subtract minutes worth of seconds from seconds
    seconds -= minutes*60

    # Start line of time
    line = '  ' + str(format(initial, ',')) + ' seconds is:'

    if(days > 0):
        line += ' ' + str(int(days)) + ' day(s)'
    if(hours > 0):
        if(days > 0 and (minutes == 0 and seconds == 0)):
            line += ' and'
        elif(days > 0):
            line += ','
        line += ' ' + str(int(hours)) + ' hour(s)'
    if(minutes > 0):
        if((days > 0 or hours > 0) and seconds == 0):
            line += ' and'
        elif(days > 0 or hours > 0):
            line += ','
        line += ' ' + str(int(minutes)) + ' minute(s)'
    if(seconds > 0):
        if(days > 0 or hours > 0 or minutes > 0):
            line += ' and'
        line += ' ' + str(int(seconds)) + ' second(s)'
    line += '.'

print(line)
