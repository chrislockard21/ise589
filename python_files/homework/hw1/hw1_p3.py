'''

@author: Chris Lockard

Problem 3:
Write a program that converts F to C and displays C in the console.

'''

# Ensures the user enters a number
try:
    F = float(input('Please provide todays temperature in F: '))

    # Calculates the temperature in C
    C = (5/9)*(F-32)

    print('Todays temperature in C is: ', format(C, '.2f'))
    
except:
    print('Please enter a number.')
