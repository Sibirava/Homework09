# Count odd digits in number
# Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def count_odd_digit(number):
    count = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        if digit % 2 == 1:
            count += 1
        else:
            count += 0
    return count


def main():
    number = int(input("Input your number: "))

    count = count_odd_digit(number)

    msg = f" There are {count} odd numbers in {number}"

    print(msg)

main()