'''
@author: Chris Lockard

HW3 Problem 2

'''

def CodeWord(filename):
    '''
    Returns a file with all CNCs removed and counts all CNCs
    '''
    # Handles errors with a helpul error message
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            new_lines = []
            count = 0
            for line in lines:
                # Checks if there are CNCs in the line
                if line.count('CNC') > 0:
                    new_lines.append(line.replace('CNC', 'XYZ'))
                    count += line.count('CNC')

            # Writes observations to a new file
            with open('CodedText.txt', 'w') as new_f:
                for line in new_lines:
                    new_f.write(line)
        return count

    except:
        print('Please enter the name of a file')

print(CodeWord('2_SampleFile.txt'))
