'''

@author: Chris Lockard

Problem 2:
Create a program that will examine a string an determine the number of
characters, digits, and special characters

'''

# Accepts string from user
string = input('Please provide a string: ')

# Creates variables that sum characters and digits
numbers = sum(character.isdigit() for character in string)
letters = sum(character.isalpha() for character in string)

# Formats a print statement that also uses the numbers/letters variables to
# calculate the special characters
print(
    'Input:\n{}\n\nOutput:\n'
    'Number of Alphabets: {}\nNumber of Digits in String is:'
    ' {}\nNumber of scpecial characters is: {}'.format(
        string, letters, numbers,
        len(string)-letters-numbers
    )
)
