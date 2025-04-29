# Imports
from dice_class import Dice


# Function
def roller(rolls_dice, user_dice):
    if rolls_dice == 1:
        print("\n" + user_dice.roll())
    elif rolls_dice > 1:
        print("\n" + user_dice.m_rolls(rolls_dice))