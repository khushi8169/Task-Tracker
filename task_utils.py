import json

def save_task(title, description, subtasks):
    task = {"title": title, "desc": description, "subtasks": subtasks}
    with open("data/tasks.json", "a") as f:
        f.write(json.dumps(task) + "\n")
    return task