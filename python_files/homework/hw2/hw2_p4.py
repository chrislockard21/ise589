'''

@author: Chris Lockard

Problem 4:
Write a function to find if a number is a prime number or not by accepting user
input. Accepts input from user and display it on the console. Modify the above
code using function to accept a range from a user and the code prints all prime
numbers till that value

'''

def prime(number):
    '''
    Determines if a number is prime or not
    '''
    # Handling if the user enters 1 or lower
    if number > 1:
        is_prime = True
        # Iterates over the range with the user input as the upper limit
        for num in range(1,number+1):
            # We know all numbers are divisable by 1 and itself so we can ignore
            # these cases
            if num != 1 and num != number:
                # If remainder is 0 for any division the number is not prime
                # Break out of the loop
                if number%num == 0:
                    is_prime = False
                    break
    else:
        # Returns false if the number is one or below
        is_prime = False
    return is_prime

# Accepts user input and prints weather the number is prime or not
number = int(input('Please enter a whole number: '))
prime_status = prime(number)
print('Prime status: ' + str(prime_status) + '\n')


# Accepts the upper limit of a range from the user
user_range = int(input('Please enter a whole number: '))

# Appends a list with all prime numbers in the range
prime_list = [str(num) for num in range(user_range + 1) if prime(num) == True]
print('All prime numbers in this range:\n' + ' '.join(prime_list))
