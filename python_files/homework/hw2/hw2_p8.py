'''

@author: Chris Lockard

Problem 8:
Let’s play Rock, Paper and Scissors. Devise a program that lets the user play
the game with the Computer for a specified number of attempts. For each
attempt, the user inputs his/her hand and the computer randomly picks one from
the list. If you know the game – Rock beats Scissors; Paper beats Rock; Scissors
beats Paper. The algorithm should also track the score for the user and the
Computer until the end of the game. Write the program using functions whenever
possible

'''

import random

def roc_p_sci(pick):
    '''
    Returns the verdict of the game
    '''

    # Defines computers choices
    choices = ['rock', 'paper', 'scissors']

    # Picks a choice
    comp_pick = random.choice(choices)

    # Logic to determine the winner
    if pick.lower() == comp_pick:
        return 'tie'
    elif pick.lower() == 'rock' and comp_pick == 'paper':
        return ('comp', comp_pick)
    elif pick.lower() == 'rock' and comp_pick == 'scissors':
        return ('user', comp_pick)
    elif pick.lower() == 'paper' and comp_pick == 'rock':
        return ('user', comp_pick)
    elif pick.lower() == 'paper' and comp_pick == 'scissors':
        return ('comp', comp_pick)
    elif pick.lower() == 'scissors' and comp_pick == 'rock':
        return ('comp', comp_pick)
    elif pick.lower() == 'scissors' and comp_pick == 'paper':
        return ('user', comp_pick)

print('Input:')
attempts = int(input('Enter number of attempts: '))
name = input('Enter your name: ')

i = 0
comp = 0
user = 0

# Determines the victor of all games and the match
while i < attempts:
    i+=1
    pick = input('\nInput:\nAttempt {}: Show your Hand: '.format(i))
    out = roc_p_sci(pick)
    if out[0] == 'comp':
        comp+=1
        print(
            '\nOutput\nSorry, you lost. Computer picked {}'
            '\nScore: User: {}; Computer: {}'.format(out[1], user, comp)
        )
    elif out[0] == 'user':
        user+=1
        print(
            '\nOutput\nYou win! Computer picked {}'
            '\nScore: User: {}; Computer: {}'.format(out[1], user, comp)
        )
    else:
        print(
            '\nOutput\nTie!'
            '\nScore: User: {}; Computer: {}'.format(user, comp)
        )

if comp > user:
    print(
        '\nOutput:\nCongradulations Computer, you won the game!'
        ' Sorry, {}, you lost.\n\nFinal Score: {} - {};'
        ' Computer - {}'.format(name, name, user, comp)

    )
elif user > comp:
    print(
        '\nOutput:\nCongradulations {}, you won the game!'
        ' Sorry, Computer, you lost.\n\nFinal Score: {} - {};'
        ' Computer - {}'.format(name, name, user, comp)
    )
else:
    print('Tie game! Thanks for playing!')
