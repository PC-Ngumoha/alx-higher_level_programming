#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except ValueError as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
    except TypeError as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
    else:
        return True
