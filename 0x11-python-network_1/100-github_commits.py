#!/usr/bin/python3
"""Requests 10 of the most recent commits to a particular repository on Github
"""
import requests
import sys


if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    token = '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'
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner,
                                                              repo_name)
    params = {'per_page': 10}
    headers = {'Authorization': 'Bearer {}'.format(token)}
    try:
        r = requests.get(url, params=params, headers=headers)
        responses = r.json()
        for response in responses:
            sha = response.get('sha')
            author_name = response.get('commit').get('author').get('name')
            print('{}: {}'.format(sha, author_name))
    except (ValueError, TypeError) as err:
        print(err)
