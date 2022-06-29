#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_value = abs(number)
if number < 0:
    last_digit = -1 * (abs_value % 10)
else:
    last_digit = abs_value % 10

if last_digit > 5:
    message = "is greater than 5"
elif last_digit == 0:
    message = "is 0"
elif last_digit < 6 and last_digit != 0:
    message = "is less than 6 and not 0"
print(f"Last digit of {number:d} is {last_digit:d} and {message}")
