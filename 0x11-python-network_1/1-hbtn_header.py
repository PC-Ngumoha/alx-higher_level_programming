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
            print(response.headers.get(desired_key))
    except HTTPError as e:
        print('Reason: {}'.format(e.reason))
    except URLError as e:
        print('Reason: {}'.format(e.reason))
