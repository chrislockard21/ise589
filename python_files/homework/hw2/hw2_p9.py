'''

@author: Chris Lockard

Problem 9:
Answer each part

'''

def vowels(string):
    '''
    Determines the number of vowels in a string
    '''
    count = 0
    vowels = 'AEIOUaeiou'
    for item in string:
        if item in vowels:
            count+=1
    return count

def consonants(string):
    '''
    Determines the number of consonants in a string
    '''
    count = 0
    consonants = 'BCDFGHJKLMNPQRSTVXZWYbcdfghjklmnpqrstvxzwy'
    for item in string:
        if item in consonants:
            count+=1
    return count

def conv_lower(string):
    '''
    Converts string to lowercase
    '''
    return string.lower()

def conv_upper(string):
    '''
    Converts string to uppercase
    '''
    return string.upper()


string = input('Please provide a string: ')

print(
    'Please specify how you would like to process the string with the menu below'
)

# Menu
print('''
        A Count the number of vowels in the string
        B Count the number of consonates in the string
        C Convert the string to uppercase
        D Convert the string to lowercase
        E Enter another string
        M Display this menu
        X Exit the program
''')

usr_in = ''

# Accepts user inputs for as long as the program is open
while usr_in != 'X':
    usr_in = input('Please select an option: ').upper()
    if usr_in == 'A':
        vow = vowels(string)
        print('There are {} vowels!\n'.format(vow))
    elif usr_in == 'B':
        con = consonants(string)
        print('There are {} consonants!\n'.format(con))
    elif usr_in == 'C':
        up = conv_upper(string)
        print('This is the string in uppercase:\n{}\n'.format(up))
    elif usr_in == 'D':
        low = conv_lower(string)
        print('This is the string in lowercase:\n{}\n'.format(low))
    elif usr_in == 'E':
        string = input('Please provide a new string: ')
        print('New string accepted:\n{}\n'.format(string))
    elif usr_in == 'M':
        print('''
        A Count the number of vowels in the string
        B Count the number of consonates in the string
        C Convert the string to uppercase
        D Convert the string to lowercase
        E Enter another string
        M Display this menu
        X Exit the program
        ''')
