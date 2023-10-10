#!/usr/bin/python3
"""Export to-do information of all emoployee to json format
using JSONPlaceholder API
(https://jsonplaceholder.typicode.com/)
"""

import json
import requests
from sys import argv

url = 'https://jsonplaceholder.typicode.com/'


if __name__ == "__main__":
    users = requests.get(url + 'users').json()
    todos = requests.get(url + 'todos').json()

    filename = 'todo_all_employees.json'

    with open(filename, 'w') as jsonfile:
        json.dump({
            u.get('id'): [{
                "username": u.get('username'),
                "task": t.get('title'),
                "completed": t.get('completed'),
                } for t in requests.get(url + "users/{}/todos"
                                        .format(u.get('id'))).json()]
            for u in users}, jsonfile)
