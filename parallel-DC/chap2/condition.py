import threading
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(threadName)s: %(message)s')

condition = threading.Condition()

def car(name):
    with condition:
        logging.info(f"{name} is ready and waiting for the start signal...")
        condition.wait()  # wait until notified
        logging.info(f"{name} started racing! 🏁")
    time.sleep(random.uniform(2, 5))
    logging.info(f"{name} finished the race!")

def race_controller():
    time.sleep(3)
    with condition:
        logging.info("🚦 Controller giving start signal!")
        condition.notify_all()  # wake all waiting cars

cars = [threading.Thread(target=car, args=(f"Car-{i}",)) for i in range(1, 4)]
controller = threading.Thread(target=race_controller, name="Controller")

for c in cars:
    c.start()
controller.start()

for c in cars:
    c.join()
controller.join()
