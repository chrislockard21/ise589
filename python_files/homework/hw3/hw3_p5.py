'''
@author: Chris Lockard

HW3 Problem 5

'''

from zipfile import *
from collections import OrderedDict

# Creates zip object
zip_archive = ZipFile('5_Jobs_Completed_log.zip', 'r')

sum = 0
# Sums value from jobs completed lines
for file in zip_archive.namelist():
    file_opened = zip_archive.open(file, 'r')
    lines = file_opened.readlines()
    total_lines = [
        line.decode('utf-8').split() for line in lines
        if line.startswith(b'Jobs Completed..')
    ]
    for line in total_lines:
        sum += int(line[2])

print(sum)
