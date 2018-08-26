'''

@author: Chris Lockard

Problem 6:
Write a program that accepts mass in kg and prints the weight of the objects
mass.

'''

# imports decimal class
from decimal import *

# Accepts user input for mass in kg
mass_kg = input('Input the mass of the car in kg: ')

# Creates decimal objects and converts kg to N
weight_N = Decimal(mass_kg) * Decimal(9.81)

# Prints the results
print(
    'Given Input (kg): '
    + str(mass_kg)
    + '\n'
    + 'Weight (N): '
    + str(round(weight_N, 0))
)
