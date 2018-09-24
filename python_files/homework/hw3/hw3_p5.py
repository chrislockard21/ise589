from zipfile import *
from collections import OrderedDict

zip_archive = ZipFile('5_Jobs_Completed_log.zip', 'r')

sum = 0
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
