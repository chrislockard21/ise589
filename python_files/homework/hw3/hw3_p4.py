'''
@author: Chris Lockard

HW3 Problem 4

'''

with open('4_NoofParts_assem.txt', 'r', encoding='utf_16') as f:
    lines = f.readlines()

    # Deletes header
    del lines[0]

    # Separates words in lines
    rows = [line.split() for line in lines]

sum = 0
parts = 0
for row in rows:
    if int(row[1]) > parts:
        id = row[0]
        parts = int(row[1])

    sum += int(row[1])

print('Part a:\nNumber of entries: {}'.format(len(rows)))
print('\n\nPart b:\nSum of parts: {}'.format(sum))
print('\n\nPart c:\nPart id (largest part): {}\nNumber of parts: {}'.format(
        id, parts
    )
)
