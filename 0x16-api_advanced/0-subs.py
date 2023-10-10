
n to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0 (by /u/Various_Ad_2057)"
        }

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subs = data.get('data').get('subscribers')
        if subs is None:
            return 0
        return subs
    else:
        return 0
