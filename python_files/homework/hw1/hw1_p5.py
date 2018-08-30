'''

@author: Chris Lockard

Problem 5:
Write a program that will dsiplay the output as shown in hw1 problem 5.

'''

# Defines lists to make for simpler printing
x = [10, 20, 20, 20, 30,]
y = [5, 5, 10, 5, 5,]
exp = [y[0]+3, y[1]-2, y[2]*5, int(x[3]/y[3]), x[4]%y[4],]
exp_str = ['x=y+3', 'x=y-2', 'x=y*5', 'x=x/y', 'x=x%y',]

print('x value\t\ty value\t\texpressions\t\tresult')

# Loops through list items to create the print
for x_print, y_print, exp_str_print, exp_print  in zip(x, y, exp_str, exp):
    print(
        '{}\t|\t{}\t|\t{}\t\t|\t{}'.format(
            x_print, y_print, exp_str_print, exp_print
        )
    )
