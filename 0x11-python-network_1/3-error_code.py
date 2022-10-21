#!/usr/bin/python3
'''A script that gets the value of a specific HTTP request header.'''
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
        print('Error Code: {}'.format(e.code))
