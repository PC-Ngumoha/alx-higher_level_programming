#!/usr/bin/python3
"""Script to access my personal Github account and print out my ID"""
import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    url = ' https://api.github.com/users/{}'.format(username)
    headers = {'Authorization': 'Bearer {}'.format(password)}
    try:
        r = requests.get(url, headers=headers)
        response = r.json()
        print(response.get('id'))
    except (ValueError, TypeError) as err:
        pass
