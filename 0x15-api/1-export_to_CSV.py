#!/usr/bin/python3
"""Script that uses JSONPlaceholder API to get information about employee
(https://jsonplaceholder.typicode.com/)
"""

import csv
import requests
from sys import argv

url = 'https://jsonplaceholder.typicode.com/'


if __name__ == "__main__":
    uurl = '{}users/{}'.format(url, argv[1])
    user = requests.get(uurl).json()
    todos = requests.get(uurl + '/todos').json()

    username = user.get('username')
    user_id = user.get('id')
    filename = '{}.csv'.format(user_id)

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        # "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
        [writer.writerow([user_id, username, t.get('completed'),
                         t.get('title')]) for t in todos]
