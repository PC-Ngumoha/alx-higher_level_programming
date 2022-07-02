#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        my_list = list(my_string)
        new_list = []
        for letter in my_list:
            if letter != 'c' and letter != 'C':
                new_list.append(letter)
        new_string = ''.join(new_list)
        return new_string
    else:
        return None
