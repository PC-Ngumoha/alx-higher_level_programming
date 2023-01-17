#!/usr/bin/python3
""" Sending data to a server which generates a JSON response """
import requests
import sys


if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    arg = "" if len(sys.argv) == 1 else sys.argv[1]
    output = requests.post(url, data={'q': arg})
    try:
        output = output.json()
        if output == {}:
            print('No result')
        else:
            print('[{}] {}'.format(output.get('id'), output.get('name')))
    except ValueError:
        print('Not a Valid JSON')
