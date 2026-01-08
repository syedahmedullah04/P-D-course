import multiprocessing
import time
import random

def download_file(file_id):
    print(f"[Process {file_id}] Starting download...")
    download_time = random.randint(2, 5)
    time.sleep(download_time)
    print(f"[Process {file_id}] Finished downloading in {download_time} seconds.\n")

if __name__ == '__main__':
    processes = []
    for i in range(5):
        process = multiprocessing.Process(target=download_file, args=(i+1,))
        processes.append(process)
        process.start() 

    for process in processes:
        process.join()

    print(" All downloads completed successfully!")
