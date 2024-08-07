#!/usr/bin/python3
"""
Fetch and export TODO list progress
"""

import json
import requests


def export_to_json():
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    all_tasks = {}

    for user in users:
        user_id = user['id']
        username = user['username']

        user_tasks = []

        for task in todos:
            if task['userId'] == user_id:
                user_tasks.append({
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                })

        all_tasks[user_id] = user_tasks

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file, indent=4)


if __name__ == "__main__":
    export_to_json()
