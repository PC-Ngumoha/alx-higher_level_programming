#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
nargs = len(argv)
if nargs == 1:
    print("{:d} arguments.".format(nargs - 1))
elif nargs > 1:
    message = "argument" if (nargs == 2) else "arguments"
    print("{:d} {:s}:".format(nargs - 1, message))
    for i in range(1, nargs):
        print("{:d}: {:s}".format(i, argv[i]))
