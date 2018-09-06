'''

@author: Chris Lockard

Problem 10:
Create a simulated lottery

'''

# Defines empty dict
dict = {}

# Numbers used to incriment the loop
inc = 3
num = 0
constant = 3

# Constant used to count down to match the pattern in the problem
while num != 100:
    num+=1
    if inc == 0:
        inc = constant*2
        constant = constant*2
    dict[num] = inc
    inc -= 1

usr_in = []

print('\nPlease only guess numbers 1 - 100!\n')

# Accepts 5 user inputs for numbers and prompts the user to guess again if the
# number is out of range
i = 1
while i < 6:
    guess = int(input('Guess number {}: '.format(i)))
    if guess in range(1, 101):
        usr_in.append(guess)
    else:
        guess = int(input('Please guess again that number was out of range: '))
    i += 1

print('\nYour guesses were:')
print(*usr_in)

# Calculates and prints the users winnings
winnings = [dict[item] for item in usr_in if dict[item]]
print('\nErin, your total winnings are: ${}'.format(sum(winnings)))
