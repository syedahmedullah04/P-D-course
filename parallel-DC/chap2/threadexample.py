import threading
import time
import os
from random import randint
from threading import Thread

account_balance = 1000  # shared resource

class BankDeposit(Thread):
    def __init__(self, name, amount, duration):
        Thread.__init__(self)
        self.name = name
        self.amount = amount
        self.duration = duration

    def run(self):
        global account_balance
        print("---> " + self.name + " started, belonging to process ID " + str(os.getpid()))
        print(f"{self.name} checking current balance: ${account_balance}")
        time.sleep(self.duration)
        account_balance += self.amount
        print(f"{self.name} deposited ${self.amount}. Updated balance: ${account_balance}")
        print("---> " + self.name + " over\n")


def main():
    start_time = time.time()
    print("\n=== Bank Account Deposit Simulation WITHOUT Lock ===\n")

    deposits = [
        BankDeposit(f"User#{i}", 200, randint(1, 3))
        for i in range(1, 6)
    ]

    for t in deposits:
        t.start()

    for t in deposits:
        t.join()

    print("All transactions completed.")
    print(f"Final Account Balance: ${account_balance}")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()