'''

@author: Chris Lockard

Problem 10:
Write a program that returns the name of the month (per user integer input)
without using conditional statements.

'''

from datetime import date

print('Input:')
month_int = int(input('Enter Integer: '))

month = date(2018, month_int, 1).strftime('%B')
print('\nOutput:\nMonth is: ' + month)
