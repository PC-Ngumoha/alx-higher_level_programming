#!/usr/bin/python3
def uppercase(string):
    for i in range(len(string)):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            letter = chr(ord(string[i]) - 32)
        else:
            letter = string[i]
        print("{:s}".format(letter,), end="")
    print()
