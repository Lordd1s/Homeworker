import json

import requests

from main import Todo

response = requests.get('https://jsonplaceholder.typicode.com/todos/1').json()
with open("jsons2.json", "w") as file:
    json.dump(response, file)
with open("jsons2.json", "r") as ree:
    read = json.load(ree)
file = Todo(userId=None, id=None, title=None, completed=None)
file_2 = Todo(userId=None, id=None, title=None, completed=None)
file_3 = Todo(userId=None, id=None, title=None, completed=None)
file_4 = Todo(userId=None, id=None, title=None, completed=None)
list_js = [file, file_2, file_3, file_4]

for i in list_js:
    res = i.serialize(read)
    print(res)