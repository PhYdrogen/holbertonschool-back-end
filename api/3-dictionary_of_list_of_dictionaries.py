#!/usr/bin/python3
""" Getting all the user and have a big dict """

if __name__ == "__main__":
    import json
    import requests

    ru_json = requests.get("https://jsonplaceholder.typicode.com/users").json()
    rt_json = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    LIST_TASKS = []
    userDict = {}
    for user in ru_json:
        EMPLOYEE_NAME = user.get("username")
        user_id = user.get("id")
        LIST_TASKS = []

        for task in rt_json:
            tmp_dict = {}
            if task.get("userId") == user_id:
                TASK_TITLE = task.get("title")
                TASK_COMPLETED_STATUS = task.get("completed")

                tmp_dict["username"] = EMPLOYEE_NAME
                tmp_dict["task"] = TASK_TITLE
                tmp_dict["completed"] = TASK_COMPLETED_STATUS

                LIST_TASKS.append(tmp_dict)

        userDict[f"{user_id}"] = LIST_TASKS
    print(userDict)
    with open("todo_all_employees.json", 'w') as f:
        f.write(json.dumps(userDict))
