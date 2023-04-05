#!/usr/bin/python3
""" using requests for api """

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    if len(argv) <= 1:
        exit(1)
    user_id = int(argv[1])

    ru_json = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}").json()
    rt_json = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    LIST_TASKS = []
    EMPLOYEE_NAME = ru_json.get('username')
    userDict = {}
    for task in rt_json:
        tmp_dict = {}
        if task.get("userId") == user_id:
            TASK_TITLE = task.get("title")
            TASK_COMPLETED_STATUS = task.get("completed")

            tmp_dict["task"] = TASK_TITLE
            tmp_dict["completed"] = TASK_COMPLETED_STATUS
            tmp_dict["username"] = EMPLOYEE_NAME

            LIST_TASKS.append(tmp_dict)

    userDict[f"{user_id}"] = LIST_TASKS
    with open(f"{user_id}.json", 'w') as f:
        f.write(json.dumps(userDict))
