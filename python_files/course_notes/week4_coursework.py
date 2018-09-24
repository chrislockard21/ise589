eol = '\n'
lines = 'binil', eol, 'starly', 'has', eol, 'been', eol, 'teaching', eol,

file = open('writelines.txt', 'w')
file.writelines(lines)
file.close()

file = open('sample.txt', 'r')
wdoc = open('copiedtext.txt', 'w')
for i, line in enumerate(file):
    print(i,line)
    print(type(line))
    wdoc.writelines(line)
wdoc.close()
file.close()

rdoc = open('sample.txt', 'r')
line_list = []
word_list = []
unique_word = []

for line in rdoc:
    line_list.append(line.split())

for line in line_list:
    for word in line:
        sword = word.strip('.')
        word_list.append(sword)
        if sword.lower() not in unique_word:
            unique_word.append(sword)

print(*unique_word)
print(len(unique_word))
print(*word_list)
print(len(word_list))
rdoc.close()

import zipfile as zp
import csv


# Zip files
zip = zp.ZipFile('5000-Sales-Records.zip')
filelist = zip.namelist()

zip.extractall()

total_order = 0
line_count = 0
with open('5000 Sales Records.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        if line_count != 0:
            total_order += int(row[8])
            line_count += 1
        else:
            line_count += 1
    print(total_order)

max_rev = 0.0
line_count = 0
with open('5000 Sales Records.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        if line_count != 0:
            if max_rev < float(row[11]):
                max_rev = float(row[11])
                max_country = row[1]
                line_count += 1
        else:
            line_count += 1
    print(max_country, max_rev)

import collections

line_count = 0
country_dict = {}
with open('5000 Sales Records.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        if line_count != 0:
            if row[1] not in country_dict.keys():
                country_dict[row[1]] = row[8]
            else:
                if row[8] > country_dict[row[1]]:
                    country_dict[row[1]] = row[8]
            line_count += 1
        else:
            line_count += 1
    sorted = collections.OrderedDict(sorted(country_dict.items()))
    for k, v in sorted.items():
        print(k, v)

line_count = 0
item_type = {}
with open('5000 Sales Records.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        if line_count != 0:
            if row[2] not in item_type.keys():
                item_type[row[2]] = [row[1]]
            else:
                item_type[row[2]].append(row[1])
            line_count += 1
        else:
            line_count += 1

    for k, v in item_type.items():
        print(k, v)


# MongoDB
import pymongo
from pymongo import MongoClient
import pprint, csv

client = MongoClient(mongodb+srv://chrislockard:@cluster0-rkwsl.mongodb.net/admin)

total_order = 0
line_count = 0
with open('5000 Sales Records.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        if line_count != 0:
            total_order += int(row[8])
            line_count += 1
        else:
            line_count += 1
    print(total_order)
