import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        print(f"Produced {i}")
        q.put(i)
        time.sleep(0.5)
    q.put(None)  # signal done

def consumer():
    while True:
        item = q.get()
        if item is None:
            break
        print(f"Consumed {item}")
        q.task_done()

threading.Thread(target=producer).start()
threading.Thread(target=consumer).start()
