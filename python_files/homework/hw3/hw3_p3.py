from zipfile import *
import pandas as pd

file_name = '3_Mfg_ZipFiles.zip'
zip_archive = ZipFile(file_name, 'r')

strings = []
for file in zip_archive.namelist():
    file_opened = zip_archive.open(file, 'r')
    lines = file_opened.readlines()
    decoded = [line.decode('utf-8', 'ignore') for line in lines]
    string = ' '.join(decoded)
    strings.append(string)
all = ' '.join(strings)

words = {}
for word in all.split():
    if word.lower() in list(words.keys()):
        words[word.lower()] += 1
    else:
        words[word.lower()] = 1
sorted = dict(sorted(words.items()))

unique = 0
for k, v in sorted.items():
    if v == 1:
        unique += 1

print(unique)
