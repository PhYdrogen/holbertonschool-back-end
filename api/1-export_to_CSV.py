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
    EMPLOYEE_NAME = ru_json.get('username')
    with open(f"{user_id}.csv", 'w') as f:
        for task in rt_json:
            if task.get("userId") == user_id:
                TASK_COMPLETED_STATUS = task.get("completed")
                TASK_TITLE = task.get("title")
                f.write(
                    f'"{user_id}",\
"{EMPLOYEE_NAME}",\
"{TASK_COMPLETED_STATUS}",\
"{TASK_TITLE}"\n')
