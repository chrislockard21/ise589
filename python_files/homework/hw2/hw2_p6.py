'''

@author: Chris Lockard

Problem 6:
Ask the user for a string and print out whether this string is a palindrome or
not. (A palindrome is a string that reads the same forwards and backwards.) Be
as efficient as possible with minimal number of lines of code to achieve the
desired output

'''

# String input by user
string = input('Please input a string: ').replace(' ', '').upper()

# Compares string with it's reverse
if string == string[::-1]:
    print('This string is a palindrome!')
else:
    print('This string is not a palindrome!')
