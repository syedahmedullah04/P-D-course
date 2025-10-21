import threading
import time
import random

barrier = threading.Barrier(3)

def worker(num):
    print(f"Worker {num} doing part 1")
    time.sleep(random.uniform(1, 3))
    print(f"Worker {num} waiting at barrier")
    barrier.wait()
    print(f"Worker {num} passed barrier")

threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
for t in threads: t.start()
for t in threads: t.join()
