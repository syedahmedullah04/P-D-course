import threading
import time
from random import randint

account_balance = 1000
threadLock = threading.Lock()

class BankDeposit(threading.Thread):
    def __init__(self, name, amount):
        threading.Thread.__init__(self)
        self.name = name
        self.amount = amount

    def run(self):
        global account_balance

        threadLock.acquire()
        print(f"{self.name} checking current balance: ${account_balance}")
        temp = account_balance
        threadLock.release()

        time.sleep(randint(1, 3))

        threadLock.acquire()
        temp += self.amount
        account_balance = temp
        print(f"{self.name} deposited ${self.amount}. Updated balance: ${account_balance}")
        threadLock.release()


def main():
    start_time = time.time()
    print("\n=== Bank Account Deposit Simulation ===\n")

    deposits = [BankDeposit(f"User#{i}", randint(100, 500)) for i in range(1, 6)]

    for t in deposits:
        t.start()

    for t in deposits:
        t.join()

    print("\nAll transactions completed.")
    print(f"Final Account Balance: ${account_balance}")
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()