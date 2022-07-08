#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is not None and type(roman_string) is str:
        symbols = ('I', 'V', 'X', 'L', 'C', 'D', 'M')
        values = (1, 5, 10, 50, 100, 500, 1000)
        strlen = len(roman_string)
        number = 0
        i = 0
        while i < strlen:
            j = 0
            while j < len(symbols):
                if roman_string[i] == symbols[j]:
                    if j % 2 == 0 and j != 6:
                        value = values[j]
                        if (i+1) < strlen:
                            if roman_string[i+1] == symbols[j+1]:
                                value = values[j+1] - value
                                i += 1
                            elif roman_string[i+1] == symbols[j+2]:
                                value = values[j+2] - value
                                i += 1
                        number += value
                    else:
                        number += values[j]
                    break
                j += 1
            i += 1
        return number
    else:
        return 0
