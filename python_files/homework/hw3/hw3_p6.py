'''
@author: Chris Lockard

HW3 Problem 6

'''

from zipfile import *
from collections import OrderedDict
import datetime as dt

def convert_str(string_date):
    '''
    Converts string to datetime object
    '''

    return dt.datetime.strptime(string_date, '%Y-%m-%d')

zip_archive = ZipFile('5_Jobs_Completed_log.zip', 'r')

sum = 0
max = 0
max_date = ''
job_lines = []
# Calculates maximum jobs and filters by date
for file in zip_archive.namelist():
    file_opened = zip_archive.open(file, 'r')
    lines = file_opened.readlines()
    total_lines = [
        line.decode('utf-8').split() for line in lines
        if line.startswith(b'Jobs Completed..')
    ]

    for line in total_lines:
        # Part a
        if (
            convert_str(line[3]).date() >= dt.datetime(2018, 8, 15).date() and
            convert_str(line[3]).date() <= dt.datetime(2018, 9, 15).date()
        ):
            sum += int(line[2])

        # Part b
        if int(line[2]) > max:
            max = int(line[2])
            max_date = convert_str(line[3]).date()
        job_lines.append(line)
# Part c
first_date = convert_str(job_lines[0][3]).date()
last_date = convert_str(job_lines[-1][3]).date()

print('Sum of all jobs completed: {}\n'.format(sum))
print('Date with the most jobs completed: {}\n'.format(max_date))
print(
    'Days between when the first and last job batches completed: {}\n'.format(
        (last_date - first_date).days
    )
)
