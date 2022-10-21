#!/usr/bin/python3
'''A script that sends a POST request to the specified URL'''
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email_addr = sys.argv[2]
    values = {}
    values['email'] = email_addr
    data = urlencode(values)
    data = data.encode('ASCII')
    req = Request(url, data)
    try:
        with urlopen(req) as response:
            output = response.read()
            print(output.decode('ASCII'))
    except HTTPError as e:
        print('Reason: {}'.format(e.reason))
    except URLError as e:
        print('Reason: {}'.format(e.reason))
