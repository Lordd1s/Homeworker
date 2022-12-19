import requests
import json
import threading


def default():
    url = requests.get("https://jsonplaceholder.typicode.com/todos/1/")
    result = url.json()
    with open("JsS.json", "w") as js_file:
        json.dump(result, js_file, indent=4)


def m_thread():
    thread_list = []
    for i in range(50 + 1):
        thread_list.append(threading.Thread(target=default))
        with open("thread/JsS.json", "w") as J_file:
            json.dump(J_file, indent=4)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()
