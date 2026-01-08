# OUTPUT:

![killing sc](https://raw.githubusercontent.com/ayanatiq01-arch/parallel-DC/f5a2cc506817e693d5970eb54eaadcd83e683ee5/P-DC/killing%20sc.JPG)

![naming sc](https://raw.githubusercontent.com/ayanatiq01-arch/parallel-DC/f5a2cc506817e693d5970eb54eaadcd83e683ee5/P-DC/naming%20sc.JPG)

![spawn s](https://raw.githubusercontent.com/ayanatiq01-arch/parallel-DC/f5a2cc506817e693d5970eb54eaadcd83e683ee5/P-DC/spawn%20s.JPG)



# Conclusion

In this chapter, we experimented with different multiprocessing techniques in Python to understand how processes can be created, managed, and terminated efficiently. The exercises covered the naming, spawning, and killing of processes, each highlighting a unique aspect of parallel execution. The naming example demonstrated how individual processes can be identified and managed distinctly, allowing for better debugging and monitoring. The spawn example showed how multiple processes can run in parallel to perform time-consuming tasks like downloading or image processing, significantly reducing overall execution time. The killing example illustrated how specific processes can be safely terminated based on user commands or conditions, ensuring resource optimization and process control.

Through these practical demonstrations, we learned how multiprocessing helps in improving performance by utilizing multiple CPU cores and enabling concurrent execution. The results confirmed that parallel programming not only increases efficiency but also enhances program scalability and responsiveness. Overall, this chapter provided a comprehensive understanding of process coordination, communication, and synchronization — key elements for developing robust and high-performance Python applications.

A daemon process runs in the background and is automatically terminated when the main program exits, even if it hasn’t finished its work.
It’s typically used for non-critical background tasks such as logging or monitoring.
Unlike normal processes, daemons do not prevent the main program from ending.
