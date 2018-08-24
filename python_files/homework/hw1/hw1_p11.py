'''

@author: Chris Lockard

Problem 11:
Write a program to concatinate the given dictionaries.

'''

dict_1 = {1:'Binil', 2:'Starly'}
dict_2 = {3:'Ben', 4:'Starly'}
dict_3 = {5:'Vineeth', 6:'Philip'}

new_dict = {}
new_dict.update(dict_1)
new_dict.update(dict_2)
new_dict.update(dict_3)
print('Expected Result:', new_dict)
