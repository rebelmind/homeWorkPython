import json
import requests
import os

url = "https://jsonplaceholder.typicode.com/todos/"
response = requests.get(url)
todos = response.json()

with open("todos.json", "w") as file:
    json.dump(todos, file, indent=4)

with open("todos.json", "r") as file:
    todos_list = json.load(file)

os.makedirs("todo_files", exist_ok=True)

for i, todo in enumerate(todos_list, start=1):
    with open(f"todo_files/todo_{i}.json", "w") as file:
        json.dump(todo, file, indent=4)
