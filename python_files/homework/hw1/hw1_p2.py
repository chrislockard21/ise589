'''

@author: Chris Lockard

Problem 2:
Write a program that accepts a users name and age as input, and writes it to
the console.

'''

print('input:')

# Assigns name variable to user input for their age
name = input('Enter your name: ')

# Assigns age variable to user input for their age
age = input('Enter your age: ')

print('Output:')

# Formats a printed statement based on user provided variables name and age
print('{}, you are {} years old.'.format(name, age))
