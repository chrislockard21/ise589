from zipfile import *
from collections import OrderedDict
import os

file_name = input('Input:\nWnter name of zip file: ')

print('Reading 3-stopwords.txt file...')

zip_archive = ZipFile(file_name, 'r')

strings = []
file_sum = 0
for file in zip_archive.namelist():
    file_sum += 1
    if file != '3-stopwords.txt':
        file_opened = zip_archive.open(file, 'r')
        lines = file_opened.readlines()
        decoded = [line.decode('utf-8', 'ignore') for line in lines]
        string = ' '.join(decoded)
        for letter in string:
            if letter.isalpha() or letter == ' ':
                continue
            else:
                string = string.replace(letter, '')
        strings.append(string)
    else:
        file_opened = zip_archive.open(file, 'r')
        lines = file_opened.readlines()
        decoded = [line.decode('utf-8', 'ignore') for line in lines]
        string = ' '.join(decoded)
        string = string.replace(',', '')
        exceptions = string.split()

all = ' '.join(strings)

words = {}
for word in all.split():
    if word.lower() in list(words.keys()) and word.lower() not in exceptions:
        words[word.lower()] += 1
    elif word.lower() not in exceptions:
        words[word.lower()] = 1
sorted = OrderedDict(sorted(words.items()))

unique = 0
for k, v in sorted.items():
    if v == 1:
        unique += 1

with open('output.txt', 'w') as f:
    for word, number in sorted.items():
        f.write(word + ' : ' + str(number) + '\n')

print(
    'Output:\n{} files detected.\nReading {} files...\nCounting words...\n'
    '{} unique words detected.\n\nOutput file {}'.format(
        file_sum, file_sum, unique, os.getcwd() + '/output.txt'
    )
)
