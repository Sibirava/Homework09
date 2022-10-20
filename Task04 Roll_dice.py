# Roll dice simulation game
# Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group


import random

def roll_dice():

    num_simulations = 0

    while num_simulations <= 100:
        num_simulations += 1
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == dice2:
            print(dice1, dice2, f"You win")
        else:
            print(dice1, dice2, f"Casino win")
    return

def main():

    msg = (roll_dice())
    print(msg)

main()
