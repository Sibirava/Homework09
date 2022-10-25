# The digits of a number form an increasing utility
# Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def check_digit_up(num):
    while num > 0:
        if num % 10 <= ((num // 10) % 10):
            return False
        else:
            return True


def check_digit_down(num):
    while num > 10:
        if num % 10 >= ((num // 10) % 10):
            return False
        else:
            return True

def main():
    num = int(input("Please input your number: "))

    if check_digit_up(num):
        msg = f"All digits of the number UP"
    elif check_digit_down(num):
        msg = f"All digits of the number DOWN"
    else:
        msg = f"Digits of number don't make any subsequence"

    print(msg)

main()