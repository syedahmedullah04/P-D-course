# gather.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = rank * 2  # each process creates some data
gathered = comm.gather(data, root=0)

if rank == 0:
    print("Gathered data:", gathered)
