# alltoall.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# create data: list of messages to send to each process
data = [rank * 10 + i for i in range(size)]
recv_data = comm.alltoall(data)

print(f"Process {rank} sent {data} and received {recv_data}")
