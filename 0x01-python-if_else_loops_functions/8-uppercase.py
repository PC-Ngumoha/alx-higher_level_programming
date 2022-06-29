#!/usr/bin/python3
def uppercase(string):
    for i in range(len(string)):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            print("{:s}".format(chr(ord(string[i]) - 32),), end="")
        else:
            print("{:s}".format(string[i],), end="")
    print()
