import threading
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(threadName)s: %(message)s')

barrier = threading.Barrier(4)  # 3 cars + 1 controller

def car(name):
    logging.info(f"{name} is ready at the starting line.")
    barrier.wait()  # wait until everyone (cars + controller) is ready
    logging.info(f"{name} started racing! 🏁")
    time.sleep(random.uniform(2, 5))
    logging.info(f"{name} finished the race!")

def race_controller():
    logging.info("Controller checking cars...")
    time.sleep(2)
    logging.info("All cars ready, starting race together!")
    barrier.wait()  # participate in barrier to release others

cars = [threading.Thread(target=car, args=(f"Car-{i}",)) for i in range(1, 4)]
controller = threading.Thread(target=race_controller, name="Controller")

for c in cars:
    c.start()
controller.start()

for c in cars:
    c.join()
controller.join()
