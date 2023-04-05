#!/usr/bin/python3
""" using requests for api """

if __name__ == "__main__":
    import requests
    from sys import argv


    if len(argv) <= 1:
        exit(1)
    user_id = int(argv[1])

    ru_json = requests.get("https://jsonplaceholder.typicode.com/users").json()
    rt_json = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    LIST_TITLE = []
    for user in ru_json:
        userId = user.get("id")
        TOTAL_NUMBER_OF_TASKS = 0
        NUMBER_OF_DONE_TASKS = 0
        LIST_TITLE = []
        if user_id == userId:
            EMPLOYEE_NAME = user.get('name')
            print(f"Employee {EMPLOYEE_NAME} is done with tasks",end="")
            for task in rt_json:
                if task.get("completed") and task.get("userId") == userId:
                    NUMBER_OF_DONE_TASKS += 1
                    LIST_TITLE.append(task.get("title"))
                if not task.get("completed") and task.get("userId") == userId:
                    TOTAL_NUMBER_OF_TASKS += 1

            print(f"({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS+NUMBER_OF_DONE_TASKS}):")
            for title in LIST_TITLE:
                print(f"\t {title}")
