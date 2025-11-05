import multiprocessing
import time
import random

def analyze_data(dataset_name):
    process_name = multiprocessing.current_process().name
    print(f"[{process_name}] Starting analysis for {dataset_name}...")
    time_to_analyze = random.randint(2, 5)
    time.sleep(time_to_analyze)
    print(f"[{process_name}] Finished analyzing {dataset_name} in {time_to_analyze} seconds.\n")

if __name__ == "__main__":
    datasets = ["Sales_Data.csv", "User_Logs.csv", "Inventory.csv"]

    analyzer1 = multiprocessing.Process(name="Analyzer 1 - Sales", target=analyze_data, args=(datasets[0],))
    analyzer2 = multiprocessing.Process(name="Analyzer 2 - Users", target=analyze_data, args=(datasets[1],))
    analyzer3 = multiprocessing.Process(target=analyze_data, args=(datasets[2],))  # unnamed (default name)

    analyzer3.daemon = True 

    analyzer1.start()
    analyzer2.start()
    analyzer3.start()

    print("\nAll analyzers started!\n")

    analyzer1.join()
    analyzer2.join()

    print("✅ Main process completed — daemon analyzer will close automatically.")
