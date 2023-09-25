#!/usr/bin/python3
"""Export information of an emoployee to json format using JSONPlaceholder API
(https://jsonplaceholder.typicode.com/)
"""

import json
import requests
from sys import argv

url = 'https://jsonplaceholder.typicode.com/'


if __name__ == "__main__":
    user_id = argv[1]
    uurl = '{}users/{}'.format(url, user_id)
    user = requests.get(uurl).json()
    todos = requests.get(uurl + '/todos').json()

    username = user.get('username')
    filename = '{}.json'.format(user_id)

    with open(filename, 'w') as jsonfile:
        json.dump({user_id: [{
            "task": t.get('title'),
            "completed": t.get('completed'),
            "username": username
            } for t in todos]}, jsonfile)
