#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and returns a list containing the titles of all hot articles for a given subreddit.
"""


def recurse(subreddit, hot_list=[]):
    """
    Queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
    """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        if hot_list == []:
            return None
        return hot_list
    posts = response.json().get('data').get('children')
    for post in posts:
        hot_list.append(post.get('data').get('title'))
    if response.json().get('data').get('after') is None:
        return hot_list
    return recurse(subreddit, hot_list)
