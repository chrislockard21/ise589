import datetime as dt
from datetime import timedelta

with open('8_deptReportstatus.txt') as f:
    lines = f.readlines()
    filt_lines = [
        line.strip('\n').split('\t') for i, line in enumerate(lines)
        if i != 1 and line != '\t\t\t\t\t\t\t\t\t\n'
    ]

def convert_str(string_date):
    import datetime as dt
    return dt.datetime.strptime(string_date, '%m/%d/%Y')

def faculty(max_line):
    return [item for item in max_line if item.startswith('Faculty')]

def faculty_occurances(*args):
    fac_count = {}
    for arg in args:
        for item in arg:
            if item.startswith('Faculty'):
                if item in fac_count:
                    fac_count[item] += 1
                else:
                    fac_count[item] = 1
    max = 0
    for k, v in fac_count.items():
        if v > max:
            max = v
            max_fac = k
    return max_fac, max

def faculty_occurances_5(*args):
    fac_count = {}
    for arg in args:
        for item in arg:
            if item.startswith('Faculty'):
                if item in fac_count:
                    fac_count[item] += 1
                else:
                    fac_count[item] = 1
                break
    return fac_count

def det_max(filt_lines, *args):
    max = 0
    for arg in args:
        for item in arg:
            try:
                if int(item) > max:
                    max = int(item)
                    location = filt_lines.index(arg)
                else:
                    continue
            except:
                continue
    return max, location

start_date = dt.datetime(2018, 7, 1).date()
time_list = []
for line in filt_lines:
    for item in line:
        try:
            compare_date = convert_str(item)
            if compare_date.date() > start_date - timedelta(days=365*5):
                time_list.append(line)
                break
        except:
            continue

max_award = det_max(filt_lines, *filt_lines)
faculty_involved = faculty(filt_lines[max_award[1]])
print('Part A:\nMax Award: {}\nFaculty Involved:'.format(max_award[0]))
for fac in faculty_involved:
    print(fac)

max_fac = faculty_occurances(*filt_lines)
print('\nPart B:')
print('{} occured the most with {} apperances!'.format(max_fac[0], max_fac[1]))

print('\nPart C:')
print('List of the highest occurances: ')
fac_5 = faculty_occurances_5(*time_list)
print([k + ': ' + str(v) for k,v in fac_5.items() if v == max(fac_5.values())])

print('\nPart D:\nList of the lowest occurances: ')
print([k + ': ' + str(v) for k,v in fac_5.items() if v == min(fac_5.values())])
