import requests
import json
import aiohttp
import asyncio
import threading
import multiprocessing
import time


# todo FIRST TASK

# url = requests.get("https://jsonplaceholder.typicode.com/todos/1/")
# result = url.json()
# with open("JsS.json", "w") as js_file:
#     json.dump(result, js_file, indent=4)


# todo SECOND TASK (SYNC)

# def sync():
#     url = requests.get("https://jsonplaceholder.typicode.com/todos")
#     result = url.json()
#     pre = "file_"
#     # c = 0
#     # for i in result:
#     #     c = c + 1
#     #     if c == 50 + 1:
#     #         break
#     #     with open(f"sync/{pre}{c}.json", "w") as saved_file:
#     #         json.dump(i, saved_file, indent=4)
#     with open(f"sync/{pre}.json", "w") as saved_file:
#         json.dump(result, saved_file, indent=4)


# todo THIRD TASK (THREADING)

def sync():

    url = requests.get("https://jsonplaceholder.typicode.com/todos")
    result = url.json()
    pre = "file_"
    with open(f"sync/{pre}.json", "w") as saved_file:
        json.dump(saved_file, indent=4)

    print("/n/n/n/n/n/n")


thread_list = []

thread_list.append(threading.Thread(target=sync))

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()
