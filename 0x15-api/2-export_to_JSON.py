#!/usr/bin/python3
"""
Fetch and export TODO list progress
"""

import json
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee and TODO list data from the API."""
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos'

    # Fetch employee data
    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("Employee not found")
        return None, None

    employee_data = employee_response.json()
    employee_name = employee_data.get('username')

    # Fetch TODO list data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Todos not found")
        return None, None

    todos_data = todos_response.json()

    # Filter TODOs for the given employee ID
    employee_todos = [todo for todo in todos_data if todo.get(
        'userId') == employee_id]

    return employee_name, employee_todos


def export_to_json(employee_id, employee_name, todos):
    """Export TODO list data to a JSON file."""
    data = {
        str(employee_id): [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": employee_name
            }
            for todo in todos
        ]
    }

    filename = f"{employee_id}.json"
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    employee_name, todos = fetch_employee_data(employee_id)
    if employee_name and todos:
        export_to_json(employee_id, employee_name, todos)
