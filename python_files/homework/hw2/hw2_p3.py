text = 'The world is round. We live in it. But perhaps the world is flat!'
print('Input Text:\n{}\n'.format(text))

search = input('Enter Search Text:\n')

number_found = text.count('is')

print("\nOutput\nThe number of times '{}' appears is: {}".format(search, number_found))
