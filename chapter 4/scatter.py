# scatter.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = None
if rank == 0:
    data = [10, 20, 30, 40]  # 4 elements for 4 processes

recv_data = comm.scatter(data, root=0)
print(f"Process {rank} got {recv_data}")
