#!/usr/bin/python3
"""A script to fetch and export TODO list progress to a CSV file for a given employee ID."""

import csv
import requests
import sys


def fetch_employee_data(employee_id):
    """Fetch employee and TODO list data from the API."""
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = f'{base_url}/users/{employee_id}'
    todos_url = f'{base_url}/todos'

    employee_response = requests.get(employee_url)
    if employee_response.status_code != 200:
        print("Employee not found")
        return None, None

    employee_data = employee_response.json()
    employee_name = employee_data.get('username')

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Todos not found")
        return None, None

    todos_data = todos_response.json()

    employee_todos = [todo for todo in todos_data if todo.get(
        'userId') == employee_id]

    return employee_name, employee_todos


def export_to_csv(employee_id, employee_name, todos):
    """Export TODO list data to a CSV file."""
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([employee_id, employee_name,
                            todo.get('completed'), todo.get('title')])

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    employee_name, todos = fetch_employee_data(employee_id)
    if employee_name and todos:
        export_to_csv(employee_id, employee_name, todos)
