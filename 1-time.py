'''
problem with time is that it skews timming results because of
    - system load
    - garbage collection
    - other processes running
'''
import time

def sleeper():
    time.sleep(1.75)

def spinlock():
    for _ in range(100_000_000):
        pass

# time.perf_counter -> elapsed real time / wall-clock time
# time.process_time -> CPU time
for function in [ sleeper, spinlock ]:
    t1 = time.perf_counter(), time.process_time()
    function()
    t2 = time.perf_counter(), time.process_time()
    print(f"{function.__name__}()")
    print(f" Real time: {t2[0] - t1[0]:.2f} seconds")
    print(f" CPU time: {t2[1] - t1[1]:.2f} seconds")
    print()

'''
sleeper()
 Real time: 1.75 seconds
 CPU time: 0.00 seconds

    - real time took 1.75 seconds since it was asleep for 1.75 seconds
    - CPU time was 0.00 secons as it took the CPU that time to finish the actual operation

spinlock()
 Real time: 1.77 seconds
 CPU time: 1.77 seconds

    - Real and CPU time is the same because it was actually doing work and occupying the CPU
'''