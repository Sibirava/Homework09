# Define if the number is polindrome
# Version 1.1.1, 18.10.2022
# Created by Katiaryna Sibirava
# QA4822 group

def define_palindrom(num):
    clone_num = num
    num1 = 0
    while clone_num > 0:
        digit = clone_num % 10
        num1 = num1*10 + digit
        clone_num = clone_num // 10
    return num1

def main():
    num = int(input("Please input your number: "))
    num1 = define_palindrom(num)

    if num == num1:
        msg = f"Palindrome"
    else:
        msg = f"Not palindrome"

    print(msg)

main()