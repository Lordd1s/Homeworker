# create class todos
# write datas to class with cycle
# save to json
import requests
import json


class Todo:

    response = requests.get("https://jsonplaceholder.typicode.com/todos/2").json()

    def form_obj(raw_data: list[dict], is_log=False) -> list[list[any]]:
        def for_sort(item: dict):
            return item["id"]

        raw_data.sort(key=for_sort)

        if is_log:
            print(raw_data)
        rows = []
        for dict_obj in raw_data:
            userid = dict_obj["userId"]
            ids = dict_obj["id"]
            title = dict_obj["title"]
            completed = dict_obj["completed"]
            row = [userid, ids, title, completed]
            rows.append(row)
        if is_log:
            print(rows)
        return rows
    form_obj([response])
    userid = response[0]
    ids = response[1]
    title = response[2]
    completed = response[3]
    print("userid: ", userid, ids, title, completed)
