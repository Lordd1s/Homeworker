import json
import requests

url = requests.get("https://jsonplaceholder.typicode.com/todos")
result = url.json()
pre = "file_"

c = 0
for i in result:
    c = c + 1
    with open(f"task_3/{pre}{c}.json", "w") as saved_file:
        json.dump(i, saved_file, indent=4)
