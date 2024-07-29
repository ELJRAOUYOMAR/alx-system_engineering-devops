#!/usr/bin/env python3
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    # Base URL of the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user_response = requests.get(f"{base_url}users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list data for the user
    todos_response = requests.get(f"{base_url}todos?userId={employee_id}")
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)

    # Print the TODO list progress
    print(f"Employee {employee_name} is done with tasks"
          f"({number_of_done_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py EMPLOYEE_ID")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("EMPLOYEE_ID must be an integer.")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)

