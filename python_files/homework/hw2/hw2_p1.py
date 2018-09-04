

a = [1, 11, 2, 3, 5, 8, 13, 10, 21, 34, 55, -1]

# a)
for item in a:
    if item < 10:
        print(item)

# b)
[print(item) for item in a if item < 10]

# c)
new_list = [item for item in a]
print(new_list)

# d)
number = int(input('Please provide a whole number: '))

[print(item) for item in a if item > number]
