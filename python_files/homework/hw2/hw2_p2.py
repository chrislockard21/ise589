string = input('Please provide a string: ')

numbers = sum(character.isdigit() for character in string)
letters = sum(character.isalpha() for character in string)

print(
    'Input:\n{}\n\nOutput:\n'
    'Number of Alphabets: {}\nNumber of Digits in String is:'
    ' {}\nNumber of scpecial characters is: {}'.format(
        string, letters, numbers,
        len(string)-letters-numbers
    )
)
