#!/usr/bin/python3
'''A script that gets the body of a HTTP response'''
from urllib.request import Request, urlopen
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            output = response.read()
            print(output.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {:s}'.format(str(e.code)))
