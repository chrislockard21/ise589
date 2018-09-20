with open('1_SampleText.txt', 'r') as f:
    lines = f.readlines()
    cleaned_lines = [line for line in lines if line.replace(' ', '') != '\n']

    with open('1_SampleText_cleaned.txt', 'w') as new_f:
        for line in cleaned_lines:
            new_f.write(line)
