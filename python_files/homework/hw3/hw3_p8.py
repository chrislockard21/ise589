with open('8_deptReportstatus.txt') as f:
    lines = f.readlines()
    filt_lines = [
        line.strip('\n').split('\t') for i, line in enumerate(lines)
        if i != 1 and line != '\t\t\t\t\t\t\t\t\t\n'
    ]

max = 0
is_max = False
for line in filt_lines:
    for item in line:
        try:
            if int(item) > max:
                max = int(item)
                is_max = True
                location = line.index(item)
            else:
                is_max = False
        except:
            continue
        faculty = []
        if is_max = True:
            faculty.append(item)


print('Maximum return: {}\nFaculty:'.format(max))
for fac in faculty:
    print(fac)

faculty = {}

for line in filt_lines:
    for i, phrase in enumerate(line):
        if i != 0:
            try:
                int(phrase)
                num = True
            except:
                num = False
            if num = False:
