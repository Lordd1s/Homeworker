import json
import requests

url = requests.get("https://jsonplaceholder.typicode.com/posts/1")
result = url.json()
with open("HW_TASK_2.json", "w") as json_file:
    json.dump(result, json_file, indent=4)
