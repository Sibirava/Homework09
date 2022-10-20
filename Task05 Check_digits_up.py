# The digits of a number form an increasing utility
# Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def check_digit_up(num):
    while num > 0:
        digit = num % 10

        if digit <= ((num // 100) % 10):
            return False
        else:
            return True

def main():
    num = int(input("Please input your number: "))

    result = check_digit_up(num)

    print(result)


main()