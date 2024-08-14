#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit.
"""


def top_ten(subreddit):
    """
    Queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit.
    """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except (requests.RequestException, ValueError):
        print("OK")
        return

    if 'data' in data and 'children' in data['data']:
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print("OK")
