import requests
import json


def default1():
    url = requests.get("https://jsonplaceholder.typicode.com/todos/1/")
    result = url.json()
    with open("JsS.json", "w") as js_file:
        json.dump(result, js_file, indent=4)


default1()
