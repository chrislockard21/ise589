'''

@author: Chris Lockard

Problem 9:
Write a program that converts specified days into years weeks and days.

'''

print('Input:')

days = int(input('Enter the number of days: '))

print('\nOutput:')
years = int(days/365)
print('Years:', years)

weeks = int((days%365)/7)
print('Weeks:', weeks)

days = (days%365)%7
print('Days:', days)
