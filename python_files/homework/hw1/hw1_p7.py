'''

@author: Chris Lockard

Problem 7:
Write a program that accepts user input for height and width, printing the area
of rectangle.

'''

print('Input:')

height = int(input('Please provide height (in): '))
width = int(input('Please provide width (in): '))

print(
    '\nOutput:\n'
    + 'The area of the rectangle is: '
    + str(width*height)
    + ' sq. in'
)
