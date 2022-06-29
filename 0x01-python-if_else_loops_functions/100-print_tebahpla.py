#!/usr/bin/python3
is_capital = False
step = 0
for i in range(26, 0, -1):
    if is_capital is True:
        letter = chr((ord('z') - step) - 32)
        step += 1
        is_capital = False
    else:
        letter = chr(ord('z') - step)
        step += 1
        is_capital = True
    print("{:s}".format(letter,), end="")
