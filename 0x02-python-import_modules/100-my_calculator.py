#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
nargs = len(argv)
if nargs != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
