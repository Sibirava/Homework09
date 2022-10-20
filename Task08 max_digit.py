# Find max digit
# Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def get_max_digit(number):
    number *= -1 if number < 0 else 1
    max_digit = 0

    while number > 0:
        digit = number % 10

        if digit == 9:
            max_digit = 9
            break

        if digit > max_digit:
            max_digit = digit
        number //= 10

    return max_digit


def main():
    number = int(input("Please input your number:  "))
    max_digit = get_max_digit(number)

    msg = f"Max digit in {number} is {max_digit} "
    print(msg)

main()