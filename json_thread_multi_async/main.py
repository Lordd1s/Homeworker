import requests
import json
import asyncio
import aiohttp
import concurrent.futures

response = requests.get("https://jsonplaceholder.typicode.com/todos/").json()


def sync_parse():
    for idx, item in enumerate(response):
        with open(f"sync/json_{idx}.json", "w") as write_file:
            json.dump(item, write_file)


def threading_parse():
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        for i in response:
            executor.submit(sync_parse)


def process_parse():
    with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
        for i in response:
            executor.submit(sync_parse)


async def async_parse():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/") as response_obj:
            data = await response_obj.json()
            for idx, item in enumerate(data):
                with open(f"temp/json_{idx}.json", "w") as file:
                    json.dump(item, file)


if __name__ == "__main__":
    # process_parse()
    asyncio.run(async_parse())
