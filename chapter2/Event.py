import threading
import time

event = threading.Event()

def waiter():
    print("Waiting for event to be set...")
    event.wait()
    print("Event is set! Proceeding...")

def setter():
    time.sleep(2)
    print("Event is being set now!")
    event.set()

threading.Thread(target=waiter).start()
threading.Thread(target=setter).start()
