#!/usr/bin/python
"""uses employee ID to output todo list"""

import requests
import sys

if __name__ == '__main__':
    id = sys.argv[1]
    info = request.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id))
    new_tasks = response.json()
    comp_tasks = [task for task in new_tasks if task.get('completed') is True]
    EMPLOYEE_NAME = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(id)).json().get('name')
    NUMBER_OF_DONE_TASKS = len(comp_tasks)
    TOTAL_NEMBER_OF_TASKS = len(new_tasks)
    print("Employee {} is done with tasks({}/{}:"
          .format(
              EMPLOYEE_NAME,
              NUMBER_OF_DONE_TASKS,
              TOTAL_NUMBER_OF_TASKS))
    for task in comp_tasks:
        print("\t " + task.get('title'))
