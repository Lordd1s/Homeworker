import requests
import json


class JSS:
    @staticmethod
    def get_json_one():
        idx = int(input("Type number in range 1-200: "))
        response = requests.get(f'https://jsonplaceholder.typicode.com/todos/{idx}').json()
        with open(f"json_one/{idx}.json", "w") as js_file:
            json.dump(response, js_file, indent=4)

    @staticmethod
    def get_json_many():
        response = requests.get('https://jsonplaceholder.typicode.com/todos/').json()
        c = 0
        for i in response:
            c += 1
            with open(f"json_many/{c}.json", "w") as js_file:
                json.dump(i, js_file, indent=4)
