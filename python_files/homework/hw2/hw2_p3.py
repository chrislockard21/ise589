'''

@author: Chris Lockard

Problem 3:
Write a program to check whether a given substring is present in the given
string and number of times it appears

'''

# Text to search
text = 'The world is round. We live in it. But perhaps the world is flat!'
print('Input Text:\n{}\n'.format(text))

# Text to search for
search = input('Enter Search Text:\n')

# Number of occurances of the substring
number_found = text.count('is')

# Prints the results
print("\nOutput\nThe number of times '{}' appears is: {}".format(
        search, number_found
    )
)
