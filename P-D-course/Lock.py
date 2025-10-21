import threading
import time

lock = threading.Lock()
counter = 0

def task():
    global counter
    for _ in range(5):
        with lock:   # Acquire + Release automatically
            temp = counter
            time.sleep(0.1)
            counter = temp + 1

threads = [threading.Thread(target=task) for _ in range(5)]
for t in threads: t.start()
for t in threads: t.join()

print("Final counter value:", counter)
