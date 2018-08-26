'''

@author: Chris Lockard

Problem 7:
Write a program that accepts user input for height and width, printing the area
of rectangle.

'''

print('Input:')

# Accepts input for the height and width of a rectanble
# Ensures the user entered a number
try:
    height = float(input('Please provide height (in): '))
    width = float(input('Please provide width (in): '))

    print(
        '\nOutput:\n'
        + 'The area of the rectangle is: '
        + str(format(width*height, '.2f'))
        + ' sq. in'
    )
    
except:
    print('Please enter a number.')
