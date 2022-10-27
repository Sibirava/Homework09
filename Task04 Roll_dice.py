# Roll dice simulation game
# Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group


import random

VALUE1_DICE1 = 1
VALUE2_DICE1 = 6
VALUE1_DICE2 = 1
VALUE2_DICE2 = 6
SIMULATION_NUM = 100

def roll_dice():
    simulation_num = 0
    dice1 = random.randint(VALUE1_DICE1, VALUE2_DICE1)
    dice2 = random.randint(VALUE1_DICE2, VALUE2_DICE2)

    while simulation_num != SIMULATION_NUM:
        simulation_num += 1
    return(dice1 + dice2)

def main():

    msg = f"The sum of dice game is {roll_dice()}"
    print(msg)

main()
