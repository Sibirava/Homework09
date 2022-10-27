# Find certain digit in number
#Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def find_digit(number, value):
    count = 0

    while number > 0:
        digit = number % 10
        number = number // 10
        if digit == value:
            count += 1
    return count

def main():
    number = int(input("Input your number:  "))
    value = int(input("Input value you want to find: "))
    count = find_digit(number, value)

    if 0 <= value <= 9:
        msg = f" {count} times number {value} occur in {number}"
    else:
        msg = f"Wrong value"

    print(msg)
main()
