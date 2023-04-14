import threading
import time
import concurrent.futures
import multiprocessing
# def multi(func):
#     def wrapper(*args):
#         with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
#             return executor.submit(func)
#     return wrapper
#
#
def square(num: int) -> list[int]:
    start = time.perf_counter()
    res = []
    for i in range(num+1):
        res.append(i ** 2)
        time.sleep(0.01)
    print(round(time.perf_counter() - start, 2), "secs")
    return res

# def multi():
#     with concurrent.futures.ProcessPoolExecutor(max_workers=10) as executor:
#         future = executor.submit(square, 1000)
#         return future.result()

if __name__ == "__main__":
    data = [1000]
    proc_list = []
    for j in data:
        proc_list.append(multiprocessing.Process(target=square, args=(j,)))
    for proc in proc_list:
        proc.start()
    # multi()