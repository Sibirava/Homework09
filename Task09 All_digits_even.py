# Find even digits in number
# Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def define_even_digit(number):

    while number > 0:
        digit = number % 10
        if digit % 2 == 0:
            number = number // 10
        else:
            return False
    return True

def main():
    number = int(input("Input your number: "))

    msg = f"{define_even_digit(number)}"

    print(msg)

main()