import multiprocessing
import time
import random
import os

def robot_task(robot_name):
    print(f"[{robot_name}] Started work! (PID: {os.getpid()})")
    for i in range(1, 6):
        time.sleep(random.randint(1, 3))
        print(f"[{robot_name}] Moved {i * 2} boxes...")
    print(f"[{robot_name}] Finished all tasks successfully!")

if __name__ == "__main__":
    robot1 = multiprocessing.Process(target=robot_task, args=("Robot-A",))
    robot2 = multiprocessing.Process(target=robot_task, args=("Robot-B",))
    robot3 = multiprocessing.Process(target=robot_task, args=("Robot-C",))

    robot1.start()
    robot2.start()
    robot3.start()

    print("\nAll robots started! Monitoring their work...\n")
    time.sleep(3)

    print("Robot-A alive:", robot1.is_alive())
    print("Robot-B alive:", robot2.is_alive())
    print("Robot-C alive:", robot3.is_alive())

    print("\n Robot-B malfunctioned! Terminating it now...")
    robot2.terminate()
    robot2.join()

    robot1.join()
    robot3.join()

    print("\n All robot operations completed or stopped!")
    print("Robot-A exit code:", robot1.exitcode)
    print("Robot-B exit code:", robot2.exitcode)
    print("Robot-C exit code:", robot3.exitcode)
