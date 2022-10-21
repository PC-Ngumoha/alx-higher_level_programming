#!/usr/bin/python3
'''A script that prints the value of a spcific HTTP response header'''
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    desired_key = 'X-Request-Id'
    r = requests.get(url)
    print(r.headers.get(desired_key))
