#!/usr/bin/python3
'''A script that gets the body of a HTTP response'''
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        url = sys.argv[1]
        req = Request(url)
        try:
            with urlopen(req) as response:
                output = response.read()
                print(output.decode('utf-8'))
        except HTTPError as e:
            print('Error code: {:s}'.format(str(e.code)))
        except Exception:
            pass
