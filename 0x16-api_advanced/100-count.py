#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
"""


def count_words(subreddit, word_list):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords
    """
    import requests

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return
    posts = response.json().get('data').get('children')
    word_count = {}
    for post in posts:
        title = post.get('data').get('title').lower().split()
        for word in word_list:
            if word.lower() in title:
                if word in word_count:
                    word_count[word] += title.count(word.lower())
                else:
                    word_count[word] = title.count(word.lower())
    for key, value in sorted(word_count.items(),
                             key=lambda x: x[1],
                             reverse=True):
        print('{}: {}'.format(key, value))
