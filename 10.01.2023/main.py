import json
import requests


class Todo:
    def __init__(self, title):
        self.title = title

    def get_title(self):
        print("title: ", self.title)

    def get_id(self):
        print("id: ", self.title)

    def get_user(self):
        print("userId: ", self.title)

    def get_completed(self):
        print("completed: ", self.title)

    @staticmethod
    def serialize(datas):
        with open('js_datas.json', "w") as file:
            json.dump(datas, file)


response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = response.json()
# print(todos)
username = []
ids = []
titles = []
comps = []
for todo in todos:
    username.append(Todo(todo['userId']))
    ids.append(Todo(todo['id']))
    titles.append(Todo(todo['title']))
    comps.append(Todo(todo['completed']))
    todo.serialize(todos)
for todo in username:
    todo.get_user()

for todo in ids:
    todo.get_id()

for todo in titles:
    todo.get_title()

for todo in comps:
    todo.get_completed()
