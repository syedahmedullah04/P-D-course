import threading
import time
import random

semaphore = threading.Semaphore(2)  # allow 2 threads at a time

def worker(num):
    with semaphore:
        print(f"Worker {num} started")
        time.sleep(random.uniform(1, 3))
        print(f"Worker {num} finished")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()
