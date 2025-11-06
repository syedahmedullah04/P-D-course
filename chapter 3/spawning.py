import multiprocessing
import time
import random

def build_parts(machine_id):
    print(f"[Machine {machine_id}] Starting production...")
    parts_to_build = random.randint(3, 6)
    for i in range(1, parts_to_build + 1):
        time.sleep(random.uniform(0.5, 1.5))
        print(f"[Machine {machine_id}] Built part {i}/{parts_to_build}")
    print(f"[Machine {machine_id}] Production complete!\n")

if __name__ == "__main__":
    processes = []

    for i in range(5):
        process = multiprocessing.Process(target=build_parts, args=(i+1,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print(" All machines have completed their production!")
