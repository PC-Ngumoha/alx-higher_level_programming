#!/usr/bin/python3
"""Requests 10 of the most recent commits to a particular repository on Github
"""
import requests
import sys


if __name__ == '__main__':
    repo_name = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner,
                                                              repo_name)
    params = {'per_page': 10}
    try:
        r = requests.get(url, params=params)
        commits = r.json()
        for commit in commits:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print('{}: {}'.format(sha, author_name))
    except Exception:
        pass
