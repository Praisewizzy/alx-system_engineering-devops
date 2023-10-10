
n that queries the Reddit API
returns a list containing the titles of all hot articles."""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """Returns a list of titles of all hot posts on a given subreddit."""
    global after

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)

    params = {
            "limit": 100,
            }

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0 (by /u/Various_Ad_2057)"
        }

    if after:
        params['after'] = after

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    after = response.json().get('data').get('after')

    data = response.json().get('data').get('children')
    [hot_list.append(post.get('data').get('title')) for post in data]

    if after is None:
        return hot_list

    return recurse(subreddit, hot_list)
