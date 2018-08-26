#--Lecture 001--

# Formating strings
#-------------------------------------------------------------------------------

text = 'Hello World'
name = 'Chris'

# Input always comes in as a string
age = int(input('Give age: '))

# Skips concatenation and lets you format with a function
print("{}, say's {}.".format(name, text))

# Newest method to format strings
# print(f"{name}, says {text}.")

# Printing and creating strings with formatting methods allows you to perform
# function calls and arethmatic operations within {}. Also variables inserted
# with format do not need to be converted to str
# print(f"{name}, say's {text}. He will be {age + 2} years old in 2 years.")


# String methods
#-------------------------------------------------------------------------------

text = 'Chris Lockard'

# Count lets you count the instances of the search parameter
print(text.count('i'))

# Returns the index of the first found search parameter
# There are probably other options you can add to change which index it will
# find
print(text.find('i'))

# Returns the length of the string (can also be done with lists). This will
# return the true length which is the last index + 1
print(len(text))

number = '5'

# Returns true or false depending on weather or not this input is a number
print(number.isdigit())

text = '     Hello     '

# Removes white space. Can add options to strip away specific characters
print(text.strip())


# Lists
#-------------------------------------------------------------------------------

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]

# Len function returns the length of a function that is one larger than the
# availible indicies
print(len(x))

# Slicing lists

print(x[0:0])
# Retunrs an empty list because slicing uses the absolute position. To retreive
# the first intity you must start at one or use the syntax below
print(x[:1])

# Prints the first three entities of a list including 0, 1, and 2 indicies
print(x[:3])

# Inriments the list by the value specified
print(x[::2])

# Slicing always reads to the left
print(x[-3:])
# This will print the last three numbers of a list

# You can append a list with another list
new = [1, 2,]

x.append(new)

# Adding list entity via index
# Insert method allows you to append items to specific indicies
g = 2

x.insert(2, g)
# Appends g to index 2 of the list

# Extend method allows you to add all entities of a list to another list
x.extend(new)

# If you copy a list and change it, the result will carry into the former list
age = [1, 2, 3, 4, 5,]

new_age = age

age.append(2)

print(age)
print(new_age)
# Both list will have the new value 2 because both lists are the same object

# Tuples
#-------------------------------------------------------------------------------

# Act the same as lists however they are not mutable
# They cannot be appended or deleted during the life of a program
# Uses less memory
# If you copy a tuple to another object, they will not be linked like lists are
y = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,)

# You can also create a tuple without using parenthesis
y = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

# A string is technically a tuple


# Dictionaries
#-------------------------------------------------------------------------------

# Keys and values
st_index = {'1':'Chris', '2':'Lockard', '3':'Tom', '4':'Phil',}

# You can print the value of a dictionary by specifying the key
print(st_index['1'])

# Prints keys and values
print(st_index.keys())
print(st_index.values())

# Updating a dictionary
st_index['5'] = 'Ethan'

# del operator allows you to delete keys (and other objects)
del st_index['1']

# Can check to see if something is in the dictionary
# Returns boolean
print('Does it exist:', '2' in st_index)


# Sets
#-------------------------------------------------------------------------------

# Use the set statement to define a set
# Pass a list of numbers if the set is numeric and just pass in the character
# values as themselves with no brackets
a = set([1,2,3,6,7,8,33,7,7,99])
b = set([3,1,6,100,3,21])

# Operations for comparing sets
print(a|b)
print(a-b)
# These help filter the sets to return what your looking for
