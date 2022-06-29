#!/usr/bin/python3
for i in range(0, 26):
    if i == 4 or i == 16:
        continue
    else:
        print(f"{chr(ord('a') + i):s}", end="")
