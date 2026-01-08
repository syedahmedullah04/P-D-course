from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(f"My rank is {rank}")

if rank == 1:
    message_to_send = "Hello from Process 1"
    destination = 3
    source = 3

    reply = comm.recv(source=source)
    comm.send(message_to_send, dest=destination)

    print(f"Process {rank} sent: '{message_to_send}' to process {destination}")
    print(f"Process {rank} received reply: '{reply}'")

if rank == 3:
    message_to_send = "Hi Process 1, message received"
    destination = 1
    source = 1

    comm.send(message_to_send, dest=destination)
    message = comm.recv(source=source)

    print(f"Process {rank} sent reply: '{message_to_send}' to process {destination}")
    print(f"Process {rank} received message: '{message}'")
