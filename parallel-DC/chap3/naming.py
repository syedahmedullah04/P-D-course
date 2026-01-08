import multiprocessing
import time
import random

def process_image(image_name):
    process_name = multiprocessing.current_process().name
    print(f"[{process_name}] Starting to process {image_name}...")
    time_to_process = random.randint(2, 5)
    time.sleep(time_to_process)
    print(f"[{process_name}] Finished {image_name} in {time_to_process} seconds.\n")

if __name__ == "__main__":
    images = ["photo1.jpg", "photo2.jpg", "photo3.jpg"]

    process1 = multiprocessing.Process(name="Image Processor 1", target=process_image, args=(images[0],))
    process2 = multiprocessing.Process(name="Image Processor 2", target=process_image, args=(images[1],))
    process3 = multiprocessing.Process(target=process_image, args=(images[2],))  # default name

    # Mark some processes as daemons
    process3.daemon = True   # This one will end automatically if main process ends

    process1.start()
    process2.start()
    process3.start()

    print("\nAll image processes started!\n")

    # Only join non-daemon ones
    process1.join()
    process2.join()

    print("All images have been processed!")
