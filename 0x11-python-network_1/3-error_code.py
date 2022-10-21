#!/usr/bin/python3
'''A script that gets the value of a specific HTTP request header.'''
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    req = Request(url)
    desired_key = 'X-Request-Id'
    try:
        with urlopen(req) as response:
            print(response.read().decode('UTF-8'))
    except HTTPError as e:
        print('Error Code: {}'.format(e.code))
    except URLError as e:
        print('Error Code: {}'.format(e.code))
