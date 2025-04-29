# Imports
from dice_class import Dice
from dice_function import roller


# Opening Message
print("===================\n=== DICE ROLLER ===\n===================")


# Cycle
while True:
    number_dice = int(input("\nDice number: "))
    rolls_dice = int(input("Number of rolls: "))

    user_dice = Dice(number_dice)

    # Nested Cycle
    while True:
        roller(rolls_dice, user_dice)

        user_continuing = input("\nRoll again? enter/x: ")

        if user_continuing == "":
            user_input = input("Same type? enter/x: ")
            if user_input == "":
                continue
            elif user_input == "x":
                break

        elif user_continuing == "x":
            # Closing Message
            print("Closing program...")
            exit()

