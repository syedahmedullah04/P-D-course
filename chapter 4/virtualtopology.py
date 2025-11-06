# virtualTopology.py
from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()

dims = [size, 1]  # simple 1D grid (can be 2D like [2,2])
cart_comm = comm.Create_cart(dims)

rank = comm.Get_rank()
coords = cart_comm.Get_coords(rank)
print(f"Process {rank} has coordinates {coords}")
