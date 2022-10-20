# define all digits in number are different
#Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def not_equal_digit(number):
    while number > 0:
        last_digit = number % 10
        number2 = number
        while number2 > 0:
            if last_digit == number2 // 10 % 10:
                return False
            number2 = number2 // 10
        number = number // 10
    return True

def main():
    number = int(input("Input your number: "))
    answer = not_equal_digit(number)

    if answer:
        msg = f"Number {number} has no equal digits"
    else:
        msg = f"Number {number} has equal digits"

    print(msg)
main()