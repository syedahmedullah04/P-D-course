THREADS SYNCHRONIZATION:

![Output Demonstration](https://raw.githubusercontent.com/ayanatiq01-arch/parallel-DC/main/P-DC/output.JPG)


🧠 Conclusion
The results show that multiprocessing performs faster than multithreading for this CPU-intensive calculation. This is because processes run on separate CPU cores, enabling true parallel execution, while threads share the same memory space and are limited by Python’s Global Interpreter Lock (GIL).

In summary, for CPU-bound tasks, multiprocessing is more efficient, whereas multithreading is better suited for I/O-bound operations such as reading files, handling network requests, or database operations.

Additionally, multiprocessing fully utilizes the available cores of a modern CPU, allowing heavy computations (like mathematical or data-processing tasks) to finish in significantly less time. However, it also comes with higher memory usage and inter-process communication overhead.

On the other hand, multithreading is lightweight, faster to start, and more memory-efficient — making it ideal for scenarios where multiple tasks need to wait for external events rather than continuously use the CPU.

Overall, choosing between multiprocessing and multithreading depends on the nature of the problem:

Use multiprocessing for computationally heavy tasks that can be divided into independent parts.

Use multithreading when tasks spend more time waiting than computing.
This experiment clearly demonstrates that understanding the type of workload is crucial to selecting the right parallelization strategy for maximum efficiency and performance.


    Use multithreading when tasks spend more time waiting than computing.

This experiment clearly demonstrates that understanding the type of workload is crucial to selecting the right parallelization strategy for maximum efficiency and performance.
>>>>>>> 6c916c9 (Added chap 2)
