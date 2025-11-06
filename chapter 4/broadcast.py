# broadcast.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = None
if rank == 0:
    data = "Hello, everyone!"  # only process 0 has data

data = comm.bcast(data, root=0)
print(f"Process {rank} received data: {data}")
