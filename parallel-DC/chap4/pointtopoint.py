from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(f"My rank is: {rank}")

if rank == 0:
    task_data = {"task": "data_analysis", "records": 5000}
    destination = 3
    comm.send(task_data, dest=destination)
    print(f"Manager sent task {task_data} to worker {destination}")

if rank == 1:
    task_data = {"task": "report_generation", "pages": 20}
    destination = 5
    comm.send(task_data, dest=destination)
    print(f"Manager sent task {task_data} to worker {destination}")

if rank == 3:
    received_task = comm.recv(source=0)
    print(f"Worker 3 received: {received_task}")
    print("Worker 3 started executing data analysis...")

if rank == 5:
    received_task = comm.recv(source=1)
    print(f"Worker 5 received: {received_task}")
    print("Worker 5 started generating report...")
