#!/usr/bin/env python3
import requests
import sys


def main():
    if len(sys.argv) != 2:
        return "Usage: python3 script.py EMPLOYEE_ID"

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        return "EMPLOYEE_ID must be an integer."

    employee_id = int(employee_id)
    base_url = "https://jsonplaceholder.typicode.com/"
    user_response = requests.get(f"{base_url}users/{employee_id}")
    if user_response.status_code != 200:
        return f"Employee with ID {employee_id} not found."

    user_data = user_response.json()
    employee_name = user_data.get("name")
    todos_response = requests.get(f"{base_url}todos?userId={employee_id}")
    todos_data = todos_response.json()
    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)

    result = (f"Employee {employee_name} is done with tasks"
              f"({number_of_done_tasks}/{total_tasks}):\n")
    for task in completed_tasks:
        result += f"\t {task.get('title')}\n"

    return result.strip()


if __name__ == "__main__":
    main()
