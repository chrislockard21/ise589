'''

@author: Chris Lockard

Problem 5:
Write a Fibonacci series algorithm with a limit specified by the user.
Display the generated numbers in a list and display the contents of the list to
the user

'''
# Starts the series
fib_start = [0, 1,]

# User inputs limit
limit = int(input('Please enter an upper limit for the Fibonacci series: '))

# Continues to append the series with new values until the limit is reached
while fib_start[-1] + fib_start[-2] < limit:
    fib_start.append(fib_start[-1] + fib_start[-2])

# Handles if the user enters number <= 0
if limit > 0:
    print('Fibonacci series:')
    print(*fib_start)
else:
    print('Please enter a valid limit')
