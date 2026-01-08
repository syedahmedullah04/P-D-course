# Chapter 2 – Threading with Lock Demonstration

## Screenshots of Output

### 1. With Lock
![With Lock](lock.JPG)

![Partial Lock](lock2.JPG)

### 3. Without Lock
![Without Lock](thread.JPG)

### 4. Rlock 
![RLock Screenshot](https://raw.githubusercontent.com/ayanatiq01-arch/parallel-DC/30e03df6b523e8ea279b4bd612715eb5154fc8ed/P-DC/Rlock%20ss.JPG)

---

## Conclusion

In this experiment, three threading cases were tested to compare execution time and data consistency using different lock mechanisms.

1. **Without Lock:**  
   - Execution Time: **~3.006 seconds**  
   - Observation: Multiple threads accessed and modified the shared variable (`account_balance`) simultaneously.  
   - Result: Faster execution but **incorrect and inconsistent** final balance due to race conditions.

2. **With Partial Lock:**  
   - Execution Time: **~3.004 seconds**  
   - Observation: Threads were synchronized during certain operations only.  
   - Result: **Improved accuracy** compared to the unlocked version, but occasional inconsistencies still occurred.

3. **With Full Lock:**  
   - Execution Time: **~11 seconds**  
   - Observation: Each thread waited for its turn to fully access and update the shared resource.  
   - Result: **Completely accurate and consistent** results, but execution was slower due to sequential thread execution.
  
4. **RLOCK:**
   - With RLock (Reentrant Lock):
   - Execution Time: ~11 seconds (similar to Full Lock)
   - Observation: RLock allowed the same thread to acquire the lock multiple times safely within nested function calls.

Result: Ensured complete data consistency like Full Lock, while maintaining flexibility for recursive or nested locking scenarios. RLock provides thread safety without risking deadlocks in recursive operations.

**Final Verdict:**  
Using a lock ensures **data accuracy and consistency** by preventing race conditions but increases **execution time**. Without a lock, threads run faster but cause data corruption. Therefore, choosing between speed and accuracy depends on the nature of the application.
