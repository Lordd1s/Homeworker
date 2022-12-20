import json
import requests
import threading
import multiprocessing
import aiohttp
import asyncio


# todo default
def syncs(count: int) -> list:
    url = requests.get("https://jsonplaceholder.typicode.com/todos/")
    result = url.json()[0:count:1]
    return result


def w_data(dict1: dict) -> None:
    with open(f"dir/file_{dict1['id']}.json", "w") as json_file:
        json.dump(dict1, json_file, indent=4)


data = syncs(50)

# todo sync
#
# for i in data:
#     w_data(i)


# todo THREADING

# thread_list = []
#
# for i in data:
#     thread_list.append(threading.Thread(target=w_data, args=(i,)))
# for j in thread_list:
#     j.start()
# for j in thread_list:
#     j.join()


# todo MULTIPROCESSING

# process_list = []
# if __name__ == '__main__':
#     for i in data:
#         process_list.append(multiprocessing.Process(target=w_data, args=(i,)))
#     for j in process_list:
#         j.start()
#     for j in process_list:
#         j.join()



# todo ASYNC

url1 = "https://jsonplaceholder.typicode.com/todos/"


async def async_data_json():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url1) as response_obj:
            data1 = await response_obj.json()
            c = 0
            for i in data1:
                c += 1
                if c == 50+1:
                    break
                with open(f"dir/new{c}.json", "w") as get_file:
                    json.dump(i, get_file, indent=4)


# async def run_def():
#     async def async_mass():
#         await asyncio.gather(*[async_data_json() for _ in range(1, 50+1)])
#
#         asyncio.run(async_mass())
#
if __name__ == "__main__":
    asyncio.run(async_data_json())
