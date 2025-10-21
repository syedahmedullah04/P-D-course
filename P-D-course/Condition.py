import threading
import time

condition = threading.Condition()
data_ready = False

def consumer():
    with condition:
        print("Consumer waiting...")
        condition.wait_for(lambda: data_ready)
        print("Consumer got data!")

def producer():
    global data_ready
    time.sleep(2)
    with condition:
        data_ready = True
        print("Producer: data ready, notifying...")
        condition.notify()

threading.Thread(target=consumer).start()
threading.Thread(target=producer).start()
