'''

@author: Chris Lockard

Problem 7:
Write a program that returns a list that contains only the elements that are
common between the lists (without duplicates). Make sure your program works on
two lists of different sizes

'''

# Defines lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 78, 21]

print('Common values in both lists:')

# Prints all common values in the two lists
print(*list(set(b).intersection(a)))
