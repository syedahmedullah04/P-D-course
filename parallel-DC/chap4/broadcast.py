from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Root process defines configuration
if rank == 0:
    learning_rate = 0.05
    print("Root process initialized learning rate:", learning_rate)
else:
    learning_rate = None

# Broadcast the learning_rate to all processes
learning_rate = comm.bcast(learning_rate, root=0)

print(f"Process {rank} received learning rate = {learning_rate}")
