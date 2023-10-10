
n that queries the Reddit API and
prints the titles of the first 10 hot posts listed
for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""

    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0 (by /u/Various_Ad_2057)"
        }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data.get('data').get('children')
        titles = [post.get('data').get('title') for post in posts]
        if titles is None:
            print('None')
        print('\n'.join(titles))
    else:
        print('None')
