# Count even digits in number
# Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def count_even_digit(number):
    count = 0
    while number > 0:
        digit = number % 10
        number = number // 10
        if digit % 2 == 0:
            count += 1
        else:
            count += 0
    return count


def main():
    number = int(input("Input your number: "))

    count = count_even_digit(number)

    msg = f" There are {count} even numbers in {number}"

    print(msg)

main()


