# -*- coding: utf-8 -*-
"""
@author: chris lockard

"""
# 1. Write a program to list the values within a list

alist = [1,4,6,32,6,3,77,3,3,6,7,7]

# Prints all items in a list
print(*alist)

for num in alist:
    # Prints all obs on one line
    # Flush will remove the items from the buffer is set to TRUE
    print(num, end=' ') # flush=FALSE

blist = ['Chris', 'Lockard', 'Tom', 'Joe']

# Enumerates list entities
for i,num in enumerate(blist, 1):
    print(i, num)


# 2. Write a program to list the values within a dictionary

blist = {1:'Chris', 2:'Lockard', 3:'Tom', 4:'Joe'}
for key, value in blist.items():
    print(key, value)

# 3. Write a program to find the sum of first 20 whole numbers.

nums = [num + 1 for num in range(20)]
print(nums)
print(sum(nums))


# 4. Write a program to read 6 numbers from the keyboard and find their sum and average

num = 0
numbers = []
while num < 6:
    numbers.append(int(input('Provide a number')))
    num+=1

print(sum(numbers))

# 5. Write a Python program that prints all the numbers from 0 to 20 except 3 and 13

for num in range(21):
    if num == 3 or num == 13:
        pass
    else:
        print(num)


'''

6. Write a Python program to construct the following pattern, using a nested for loop.

~
~ ~
~ ~ ~
~ ~ ~ ~
~ ~ ~ ~ ~
~ ~ ~ ~
~ ~ ~
~ ~
~

'''

for i in range(int(10/2)):
    for j in range(i):
        print('~', end=' ')
    print()
for i in range(int(10/2), 0, -1):
    for j in range(i):
        print('~', end=' ')
    print()

# 7. Write a program to iterate through a list and create a new list that contains the square of the values in the original list

first = [1,2,3,4,5,6,7,8,9,10]

second = [num**2 for num in first]

print(second)


# 8 Find Movies that start with a letter G using List Comprehension

movies = ["Star Wars", "Batman", "Gone with the Wind", "Shawshank Redemption", "Casablance", "Spiderman", "Groundhog Day", "Ghostbusters"]

movie_names_g = [movie for movie in movies if movie.startswith('G')]

print(movie_names_g)

# 9 Find the cartesian product of 2 lists or sets A X B
A = [1, 4, 6, 7]
B = [2, 4, 1, 1]

cartprod = [(a,b) for a in A for b in B]

print(cartprod)

# 10 Take 2 unequal list and create a new list that contains only numbers common to both lists
A=[1, 5, 2, 5, 33, 10, 2]
B=[50, 20, 1, 4, 22, 11, 3, 6, 50, 20, 10, 3, 55]

new_list = [b for a in A for b in B if a==b]
print(new_list)


# Generating random numbers
#-------------------------------------------------------------------------------

import random

counter = 0
chances = 6

name = input('What is your name: ').capitalize()

print('Well {}, we are going to play the game of Guess!'.format(name))

comp_guess = random.randint(1,20)

while counter < 6:
    guess = int(input('Guess a whole number between 1 and 20: '))
    if guess <= 20 and guess >=0:
        counter+=1
        if guess == comp_guess:
            print('You win the number was {}'.format(guess))
            break
    else:
        print('Number out of range, guess again!')
