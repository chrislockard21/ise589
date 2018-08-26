'''

@author: Chris Lockard

Problem 10:
Write a program that returns the name of the month (per user integer input)
without using conditional statements.

'''

print('Input:')

try:
    month_int = input('Enter Integer: ')

    # Defines dictionary to look up month names
    month_dict = {
        '1':'January', '2':'February', '3':'March', '4':'April', '5':'May',
        '6':'June', '7':'July', '8':'August', '9':'September', '10':'October',
        '11':'November', '12':'December',
    }

    print('Month is:', month_dict[month_int])

except:
    print('Please enter a whole number between 1 and 12.')
