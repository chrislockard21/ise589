'''

@author: Chris Lockard

Problem 4:
Write a function to find if a number is a prime number or not by accepting user
input. Accepts input from user and display it on the console. Modify the above
code using function to accept a range from a user and the code prints all prime
numbers till that value

'''

def prime(number):
    number_eval = int(input(prime))
    is_prime = True
    for num in range(number):
        if number%num != 0:
            is_prime = False
    return is_prime
