#!/usr/bin/python3
'''A python script that fetches the contents of a URL from a server and display
to the screen.'''
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

if __name__ == '__main__':
    req = Request('https://alx-intranet.hbtn.io/status')
    try:  # Error-prone code
        with urlopen(req) as response:
            data = response.read()
            print('Body response:')
            print('\t- type: {}'.format(type(data)))
            print('\t- content: {}'.format(data))
            print('\t- utf8 content: {}'.format(data.decode('UTF-8')))
    except HTTPError as e:
        print('Reason: {}'.format(e.reason))
    except URLError as e:
        print('Reason: {}'.format(e.reason))
