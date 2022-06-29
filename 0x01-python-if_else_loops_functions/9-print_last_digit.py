#!/usr/bin/python3
def print_last_digit(number):
    abs_number = abs(number)
    last_digit = abs_number % 10
    print("{:d}".format(last_digit,), end="")
    return last_digit
