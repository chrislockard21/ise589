'''

@author: Chris Lockard

Problem 6:
Write a program that accepts mass in kg and prints the weight of the objects
mass.

'''

from decimal import *

mass_kg = input('Input the mass of the car in kg: ')

weight_N = Decimal(mass_kg) * Decimal(9.81)

print(
    'Given Input (kg): '
    + str(mass_kg)
    + '\n'
    + 'Weight (N): '
    + str(round(weight_N, 0))
)
