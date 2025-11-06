# deadLockProblems.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = "Hello"
    comm.send(data, dest=1)
    msg = comm.recv(source=1)  # waits for reply
    print(f"Process 0 got reply: {msg}")

elif rank == 1:
    # DEADLOCK: receiving after sending can fix it
    msg = comm.recv(source=0)
    comm.send("Hi", dest=0)
    print("Process 1 replied.")
