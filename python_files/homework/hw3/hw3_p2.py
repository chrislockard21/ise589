def CodeWord(filename):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            new_lines = []
            count = 0
            for line in lines:
                if line.count('CNC') > 0:
                    new_lines.append(line.replace('CNC', 'XYZ'))
                    count += line.count('CNC')

            with open('CodedText.txt', 'w') as new_f:
                for line in new_lines:
                    new_f.write(line)
        return count
        
    except:
        print('Please enter the name of a file')

print(CodeWord('2_SampleFile.txt'))
