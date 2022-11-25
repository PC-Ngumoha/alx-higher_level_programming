#!/usr/bin/python3
'''A script that sends a request to a server and displays the response.'''
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2:
        url = sys.argv[1]
        r = requests.get(url)
        if r.status_code >= 400:
            print('Error code: {}'.format(r.status_code))
        else:
            print(r.text)