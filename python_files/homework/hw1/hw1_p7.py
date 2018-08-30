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
    prem_mult = float(2)
    print(prem_mult*height)
    print(
        '\nOutput:\n'
        + 'The area of the rectangle is: '
        + str(format(width*height, '.0f'))
        + ' sq. in\n'
        + 'The perimeter of the rectangle is: '
        + str(format((width*prem_mult)+(height*prem_mult), '.0f'))
        + ' in'
    )

except:
    print('Please enter a number.')
