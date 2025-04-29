# Imports
import random


# Class definition
class Dice:
    
    # Initializer
    def __init__(self, sides):
        self.sides = sides

    # String
    def __str__(self):
        return f"d{self.sides}"

    # Individual Roller Function
    def roll(self):
        return f"Roll: {random.randint(1, self.sides)}"

    # Multiple Roller Function + Mean
    def m_rolls(self, number):
        values = []
        for nr in range(0, number):
            values.append(random.randint(1, self.sides))
        mean = sum(values) // number
        return f"Rolls: {values}" + f"\nMean: {mean}"


# Output

# - Class
# d = Dice(20)

# print(d.roll())
# print()
# print(d.m_rolls(7))
# print()
# print(d)

# TOGGLE COMMENTS: ctrl + ~