# Find equal digits in number
#Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def equal_digit(number):
    digit = 0

    while number > 0:
        digit = number % 10
        number //= 10
        if digit == ((number // 100) % 10):
            return True
        else:
            return False

def main():
    number = int(input("Input your number"))
    answer = equal_digit(number)

    print(answer)

main()