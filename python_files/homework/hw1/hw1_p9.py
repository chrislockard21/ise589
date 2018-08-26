'''

@author: Chris Lockard

Problem 9:
Write a program that converts specified days into years weeks and days.

'''

print('Input:')

# Ensures the value the user enters is a whole number
try:
    days = int(input('Enter the number of days: '))

    # Calculates the years from the total days
    print('\nOutput:')
    years = int(days/365)
    print('Years:', years)

    # Uses the remainder of the years calculation to find the weeks
    weeks = int((days%365)/7)
    print('Weeks:', weeks)

    # Uses the remainder of the weeks calculation to find the days (the remainder
    # of the weeks calculation)
    days = (days%365)%7
    print('Days:', days)
    
except:
    print('Please enter a whole number')
