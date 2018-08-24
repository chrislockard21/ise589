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
print(f"{name}, say's {text}.")

# Printing and creating strings with formatting methods allows you to perform
# function calls and arethmatic operations within {}. Also variables inserted
# with format do not need to be converted to str
print(f"{name}, say's {text}. He will be {age + 2} years old in 2 years.")


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
