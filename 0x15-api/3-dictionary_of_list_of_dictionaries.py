#!/usr/bin/python3
"""
Fetch and export TODO list progress
"""

import json
import requests


def export_to_json():
    # API URLs
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Fetch data from the API
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Dictionary to store the tasks of all employees
    all_tasks = {}

    # Process each user
    for user in users:
        user_id = user['id']
        username = user['username']

        # List to store tasks for the current user
        user_tasks = []

        # Filter tasks for the current user
        for task in todos:
            if task['userId'] == user_id:
                user_tasks.append({
                    "username": username,
                    "task": task['title'],
                    "completed": task['completed']
                })

        # Add the user's tasks to the main dictionary
        all_tasks[user_id] = user_tasks

    # Write the data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file, indent=4)


if __name__ == "__main__":
    export_to_json()
