#!/usr/bin/python3
def remove_char_at(string, index):
    if index >= 0:
        new_string = "{:s}{:s}".format(string[:index], string[index+1:])
        return new_string
    else:
        new_string = string
        return new_string
