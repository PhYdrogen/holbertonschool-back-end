#!/usr/bin/python3
""" using requests for api """

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) <= 1:
        exit(1)
    user_id = int(argv[1])

    ru_json = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}").json()
    rt_json = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    LIST_TITLE = []
    TOTAL_NUMBER_OF_TASKS = 0
    NUMBER_OF_DONE_TASKS = 0
    EMPLOYEE_NAME = ru_json.get('name')
    for task in rt_json:
        if task.get("completed") and task.get("userId") == user_id:
            NUMBER_OF_DONE_TASKS += 1
            LIST_TITLE.append(task.get("title"))
        if not task.get("completed") and task.get("userId") == user_id:
            TOTAL_NUMBER_OF_TASKS += 1

    print(f1 := f"Employee {EMPLOYEE_NAME} is done with tasks", end="")
    print(f2 := f"({NUMBER_OF_DONE_TASKS}/\
{TOTAL_NUMBER_OF_TASKS+NUMBER_OF_DONE_TASKS}):")
    for title in LIST_TITLE:
        print(f"\t {title}")

