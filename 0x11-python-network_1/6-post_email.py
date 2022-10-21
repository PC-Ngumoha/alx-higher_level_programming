#!/usr/bin/python3
'''A script that posts an email to a server.'''
import requests
import sys


if __name__ == '__main__':
    url = sys.argv[1]
    email_addr = sys.argv[2]
    r = requests.post(url, data={'email': email_addr})
    print(r.text)
