# https://picsum.photos/200/300
import json
import requests
import time
import threading

start = time.perf_counter()


def sync():
    url1 = requests.get("https://picsum.photos/200/300").content
    # result1 = url1.content()
    pre1 = "file_"
    c = 0
    for i in url1:
        c = c + 1
        if c == 200 + 1:
            break
        with open(f"img/{pre1}{c}.jpg", "w") as saved_file1:
            json.dump(i, saved_file1)


sync()

stop = time.perf_counter()

# todo THIRD TASK (THREADING)
start1 = time.perf_counter()

url = requests.get("https://picsum.photos/200/300").content


def m_thread():
    url = requests.get("https://picsum.photos/200/300").content
    # result = url.json()
    pre = "file_"
    # print(url, type(url))
    # print(result, type(result))

    with open(f"thread/{pre}{a}.jpg", "w") as saved_file:
        json.dump(x, saved_file)


if __name__ == '__main__':
    thread_list = []
    a = 0
    for x in url:
        a = a + 1
        if a == 200 + 1:
            break
        thread_list.append(threading.Thread(target=m_thread))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
stop1 = time.perf_counter()

print(stop1 - start1)
print(stop - start)
