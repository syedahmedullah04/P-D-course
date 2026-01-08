import threading
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(threadName)s: %(message)s')

# Shared RLock for synchronization
race_lock = threading.RLock()
race_started = False  # shared flag to coordinate start

def car(name):
    global race_started
    logging.info(f"{name} is ready at the starting line.")
    
    # Wait until race starts
    while True:
        with race_lock:
            if race_started:
                break
        time.sleep(0.2)
    
    with race_lock:
        logging.info(f"{name} started racing! 🏁")
    
    time.sleep(random.uniform(2, 5))
    
    with race_lock:
        logging.info(f"{name} finished the race!")

def race_controller():
    global race_started
    with race_lock:
        logging.info("Controller checking cars...")
    time.sleep(2)
    
    with race_lock:
        race_started = True
        logging.info("All cars ready, race started! 🚦")

# Threads
cars = [threading.Thread(target=car, args=(f"Car-{i}",)) for i in range(1, 4)]
controller = threading.Thread(target=race_controller, name="Controller")

for c in cars:
    c.start()
controller.start()

for c in cars:
    c.join()
controller.join()
